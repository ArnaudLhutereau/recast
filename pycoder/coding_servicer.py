"""Wrapper for pyeclib encoders using GRPC"""
from ConfigParser import ConfigParser
import os
import logging
import logging.config

from pyeclib.ec_iface import ECDriver
from pyeclib.ec_iface import ECBackendInstanceNotAvailable
from pyeclib.ec_iface import ECBackendNotSupported
from pyeclib.ec_iface import ECInvalidParameter
from pyeclib.ec_iface import ECOutOfMemory
from pyeclib.ec_iface import ECDriverError

from playcloud_pb2 import BetaEncoderDecoderServicer
from playcloud_pb2 import DecodeReply
from playcloud_pb2 import EncodeReply
from playcloud_pb2 import Strip

from safestore.xor_driver import XorDriver
from safestore.hashed_splitter_driver import HashedSplitterDriver
from safestore.signed_splitter_driver import SignedSplitterDriver
from safestore.signed_hashed_splitter_driver import SignedHashedSplitterDriver
from safestore.aes_driver import AESDriver
from safestore.shamir_driver import ShamirDriver
from safestore.assymetric_driver import AssymetricDriver

CONFIG = ConfigParser()
CONFIG.read(os.path.join(os.path.dirname(__file__), "pycoder.cfg"))

#TODO: No absolute path
log_config = os.getenv("LOG_CONFIG", "/usr/local/src/app/logging.conf")
logging.config.fileConfig(log_config)

logger = logging.getLogger("pycoder")


def should_be_deactivated(message):
    """
    Determines whether a message stands for an option to be turned off.
    Args:
        message(str): A message to test
    Returns:
        bool: True if the message is negative, False otherwise
    """
    NEGATIVE_TERMS = ["deactivated", "disabled", "false", "no", "none", "off"]
    return message.strip().lower() in NEGATIVE_TERMS

class DriverFactory():

    def __init__(self, config):

        #ignoring config for now
        self.config = config

        if os.environ.has_key("splitter"):
            self.splitter = os.environ.get("splitter")
        elif self.config.has_option("main", "splitter"):
            self.splitter = self.config.get("main", "splitter")
        else:
            raise RuntimeError("A value must be defined for the splitter to use either in pycoder.cfg or as an environment variable SPLITTER")

        if os.environ.has_key("sec_measure"):
            self.sec_measure = os.environ.get("sec_measure")
        elif self.config.has_option("main", "sec_measure"):
            self.sec_measure = self.config.get("main", "sec_measure")
        else:
            raise RuntimeError("A value must be defined for the security measure to use either in pycoder.cfg or as an environment variable SEC_MEASURE")


    def setup_driver(self):

        splitters = {'xor': self.xor,
                     'shamir': self.shamir,
                     'ec': self.erasure_driver,
                     'aes': self.aes_driver
                    }

        self.splitter_driver = splitters[self.splitter]()

        measures = {  # just confidentiality
            'confd': self.confd,
            # confidentiality and integrity
            'confd_int': self.confd_int,
            # confidentiality and non-repudiation
            'confd_sign': self.confd_sign,
            # every guarantee
            'confd_int_sign': self.confd_int_sign}

        return measures[self.sec_measure]()

    def confd(self):
        return self.splitter_driver

    def confd_int(self):
        hash = os.environ.get("hash")
        driver = HashedSplitterDriver(self.splitter_driver, hash)
        return driver

    def _get_signer(self):
        sign_cypher = os.environ.get("signature")
        hash = os.environ.get("hash")
        key_size = int(os.environ.get("keysize"))
        return AssymetricDriver(sign_cypher, key_size, hash)

    def confd_sign(self):
        signer = self._get_signer()
        return SignedSplitterDriver(self.splitter_driver, signer)

    def confd_int_sign(self):
        signer = self._get_signer()
        return SignedHashedSplitterDriver(self.confd_int(), signer)

    def xor(self):
        nblocks = int(os.environ.get("n_blocks"))
        logger.info("{} nblocks".format(nblocks))
        return XorDriver(nblocks)

    def shamir(self):
        nblocks = int(os.environ.get("n_blocks"))
        threshold = int(os.environ.get("threshold"))

        logger.info("{} nblocks and {} threshold".format(nblocks, threshold))

        return ShamirDriver(nblocks, threshold)

    def erasure_driver(self):
        ec_k = None
        if os.environ.has_key("k"):
            ec_k = int(os.environ.get("k"))
        elif self.config.has_option("ec", "k"):
            ec_k = int(self.config.get("ec", "k"))
        else:
            raise RuntimeError("A value must be defined for the numer of data fragments (k) to use either in pycoder.cfg or as an environment variable K")

        ec_m = None
        if os.environ.has_key("m"):
            ec_m = int(os.environ.get("m"))
        elif self.config.has_option("ec", "m"):
            ec_m = int(self.config.get("ec", "m"))
        else:
            raise RuntimeError("A value must be defined for the number of parity fragments (m) to use either in pycoder.cfg or as an environment variable M")

        ec_type = None
        if os.environ.has_key("type"):
            ec_type = os.environ.get("type")
        elif self.config.has_option("ec", "type"):
            ec_type = self.config.get("ec", "type")
        else:
            raise RuntimeError("A value must be defined for the erasure coding type to use either in pycoder.cfg or as an environment variable TYPE")
        logger.info("ec_k %d, ec_m %d, ec_type %s", ec_k, ec_m, ec_type)
        # AES encryption is activated by default when using erasure coding
        # To deactivate it, set the aes env variable or aes in the main section of pycoder.cfg
        # to off
        aes_enabled = True
        if os.environ.has_key("aes") and should_be_deactivated(os.environ.get("aes")):
            aes_enabled = False
        elif self.config.has_option("main", "aes") and should_be_deactivated(self.config.get("main", "aes")):
            aes_enabled = False
        return Eraser(ec_k, ec_m, ec_type, aes_enabled=aes_enabled)

    def aes_driver(self):
        return AESDriver()

    def get_driver(self):
        return self.setup_driver()





class Eraser(object):

    """A wrapper for pyeclib erasure coding driver (ECDriver)"""

    def __init__(self, ec_k, ec_m, ec_type="liberasurecode_rs_vand", aes_enabled=True):
        self.ec_type = ec_type
        if aes_enabled:
            self.aes = AESDriver()
            logger.info("Eraser will use AES encryption")
        else:
            logger.info("Eraser will not use AES encryption")
        expected_module_name = "drivers." + ec_type.lower() + "_driver"
        expected_class_name = ec_type[0].upper() + ec_type[1:].lower() + "Driver"
        try:
            mod = __import__(expected_module_name, fromlist=[expected_class_name])
            driver_class = None
            driver_class = getattr(mod, expected_class_name)
            self.driver = driver_class(k=ec_k, m=ec_m, ec_type=ec_type, hd=None)
        except ImportError, AttributeError:
            logger.exception("Driver " + ec_type + " could not be loaded as a custom driver")
            try:
                self.driver = ECDriver(k=ec_k, m=ec_m, ec_type=ec_type)
            except Exception as error:
                logger.exception("Driver " + ec_type + " could not be loaded by pyeclib")
                raise error

    def encode(self, data):
        """Encode a string of bytes in flattened string of byte strips"""
        payload = data
        if hasattr(self, 'aes'):
            payload = self.aes.encode(data)[0]
        strips = self.driver.encode(payload)
        return strips

    def decode(self, strips):
        """Decode byte strips in a string of bytes"""
        payload = self.driver.decode(strips)
        if hasattr(self, 'aes'):
            return self.aes.decode([payload])
        return payload


class HashedDriver():

    """
    Encapsulating driver for encryption schemes with hash.
    Converts the [(block, digest)] in to a list of [block, digest]
    when encoding.
    When decoding it converts the other way around.
    """


class Eraser(object):
    """A wrapper for pyeclib erasure coding driver (ECDriver)"""

    def __init__(self, k=8, m=2, ec_type="liberasurecode_rs_vand"):
        self.k=k
        self.m=m
        self.ec_type=ec_type
        if EC_TYPE == "pylonghair":
            self.driver=PylonghairDriver(k=EC_K, m=EC_M, ec_type=EC_TYPE)
        elif EC_TYPE == "striping" or EC_TYPE == "bypass":
            self.driver=ECStripingDriver(k=EC_K, m=0, hd=None)
        else:
            self.driver=ECDriver(k=EC_K, m=EC_M, ec_type=EC_TYPE)

    def encode(self, data):
        """Encode a string of bytes in flattened string of byte strips"""
        strips=self.driver.encode(data)
        return strips_to_bytes(strips)

    def decode(self, data):
        """Decode a flattened string of byte strips in a string of bytes"""
        strips=bytes_to_strips(self.k, self.m, data)
        return self.driver.decode(strips)


class CodingService(BetaEncoderDecoderServicer):

    """
    An Encoder/Decoder built on top of playcloud.proto that can be loaded by a
    GRPC server
    """

    def Encode(self, request, context):
        """Encode data sent in an EncodeRequest into a EncodeReply"""
        try:
            reply = EncodeReply()
            logger.info("Received encode request")
            raw_strips = self.driver.encode(request.payload)

            log_temp = "Encoded and returned {} raw_strips"
            logger.debug(log_temp.format(len(raw_strips)))

            strips = []
            for raw_strip in raw_strips:
                strip = Strip()
                strip.data = raw_strip
                strips.append(strip)

            reply.strips.extend(strips)
            reply.parameters["splitter"] = os.environ.get("splitter", CONFIG.get("main", "splitter"))
            log_temp = "Request encoded, returning reply with {} strips"
            logger.info(log_temp.format(len(strips)))
            return reply
        except (ECBackendInstanceNotAvailable, ECBackendNotSupported, ECInvalidParameter, ECOutOfMemory, ECDriverError) as error:
            logger.exception("An exception was while caught encoding blocks")
            raise error

    def Decode(self, request, context):
        """Decode data sent in an DecodeRequest into a DecodeReply"""
        try:
            logger.info("Received decode request")

            reply = DecodeReply()
            strips = convert_strips_to_bytes_list(request.strips)
            reply.dec_block = self.driver.decode(strips)
            reply.parameters["splitter"] = os.environ.get("splitter", CONFIG.get("main", "splitter"))
            logger.info("Request decoded, returning reply")
            return reply
        except (ECBackendInstanceNotAvailable, ECBackendNotSupported, ECInvalidParameter, ECOutOfMemory, ECDriverError) as error:
            logger.exception("An exception was while caught decoding blocks")
            raise error
