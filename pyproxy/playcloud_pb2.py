# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playcloud.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='playcloud.proto',
  package='',
  syntax='proto3',
  serialized_pb=b'\n\x0fplaycloud.proto\"\x15\n\x05Strip\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x87\x01\n\rEncodeRequest\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x32\n\nparameters\x18\x02 \x03(\x0b\x32\x1e.EncodeRequest.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8a\x01\n\x0b\x45ncodeReply\x12\x16\n\x06strips\x18\x01 \x03(\x0b\x32\x06.Strip\x12\x30\n\nparameters\x18\x02 \x03(\x0b\x32\x1c.EncodeReply.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8e\x01\n\rDecodeRequest\x12\x16\n\x06strips\x18\x01 \x03(\x0b\x32\x06.Strip\x12\x32\n\nparameters\x18\x02 \x03(\x0b\x32\x1e.DecodeRequest.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x85\x01\n\x0b\x44\x65\x63odeReply\x12\x11\n\tdec_block\x18\x01 \x01(\x0c\x12\x30\n\nparameters\x18\x02 \x03(\x0b\x32\x1c.DecodeReply.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1e\n\x0c\x42lockRequest\x12\x0e\n\x06\x62locks\x18\x01 \x01(\r\"$\n\nBlockReply\x12\x16\n\x06strips\x18\x01 \x03(\x0b\x32\x06.Strip2d\n\x0e\x45ncoderDecoder\x12(\n\x06\x45ncode\x12\x0e.EncodeRequest\x1a\x0c.EncodeReply\"\x00\x12(\n\x06\x44\x65\x63ode\x12\x0e.DecodeRequest\x1a\x0c.DecodeReply\"\x00\x32\x38\n\x05Proxy\x12/\n\x0fGetRandomBlocks\x12\r.BlockRequest\x1a\x0b.BlockReply\"\x00\x42\x19\n\x17\x63h.unine.iiun.safecloudb\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STRIP = _descriptor.Descriptor(
  name='Strip',
  full_name='Strip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Strip.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=40,
)


_ENCODEREQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='EncodeRequest.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='EncodeRequest.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='EncodeRequest.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=178,
)

_ENCODEREQUEST = _descriptor.Descriptor(
  name='EncodeRequest',
  full_name='EncodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='EncodeRequest.payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='EncodeRequest.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENCODEREQUEST_PARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=178,
)


_ENCODEREPLY_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='EncodeReply.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='EncodeReply.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='EncodeReply.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=178,
)

_ENCODEREPLY = _descriptor.Descriptor(
  name='EncodeReply',
  full_name='EncodeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strips', full_name='EncodeReply.strips', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='EncodeReply.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENCODEREPLY_PARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=319,
)


_DECODEREQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='DecodeRequest.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DecodeRequest.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DecodeRequest.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=178,
)

_DECODEREQUEST = _descriptor.Descriptor(
  name='DecodeRequest',
  full_name='DecodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strips', full_name='DecodeRequest.strips', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='DecodeRequest.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DECODEREQUEST_PARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=322,
  serialized_end=464,
)


_DECODEREPLY_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='DecodeReply.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DecodeReply.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DecodeReply.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=178,
)

_DECODEREPLY = _descriptor.Descriptor(
  name='DecodeReply',
  full_name='DecodeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dec_block', full_name='DecodeReply.dec_block', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='DecodeReply.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DECODEREPLY_PARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=600,
)


_BLOCKREQUEST = _descriptor.Descriptor(
  name='BlockRequest',
  full_name='BlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks', full_name='BlockRequest.blocks', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=602,
  serialized_end=632,
)


_BLOCKREPLY = _descriptor.Descriptor(
  name='BlockReply',
  full_name='BlockReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strips', full_name='BlockReply.strips', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=670,
)

_ENCODEREQUEST_PARAMETERSENTRY.containing_type = _ENCODEREQUEST
_ENCODEREQUEST.fields_by_name['parameters'].message_type = _ENCODEREQUEST_PARAMETERSENTRY
_ENCODEREPLY_PARAMETERSENTRY.containing_type = _ENCODEREPLY
_ENCODEREPLY.fields_by_name['strips'].message_type = _STRIP
_ENCODEREPLY.fields_by_name['parameters'].message_type = _ENCODEREPLY_PARAMETERSENTRY
_DECODEREQUEST_PARAMETERSENTRY.containing_type = _DECODEREQUEST
_DECODEREQUEST.fields_by_name['strips'].message_type = _STRIP
_DECODEREQUEST.fields_by_name['parameters'].message_type = _DECODEREQUEST_PARAMETERSENTRY
_DECODEREPLY_PARAMETERSENTRY.containing_type = _DECODEREPLY
_DECODEREPLY.fields_by_name['parameters'].message_type = _DECODEREPLY_PARAMETERSENTRY
_BLOCKREPLY.fields_by_name['strips'].message_type = _STRIP
DESCRIPTOR.message_types_by_name['Strip'] = _STRIP
DESCRIPTOR.message_types_by_name['EncodeRequest'] = _ENCODEREQUEST
DESCRIPTOR.message_types_by_name['EncodeReply'] = _ENCODEREPLY
DESCRIPTOR.message_types_by_name['DecodeRequest'] = _DECODEREQUEST
DESCRIPTOR.message_types_by_name['DecodeReply'] = _DECODEREPLY
DESCRIPTOR.message_types_by_name['BlockRequest'] = _BLOCKREQUEST
DESCRIPTOR.message_types_by_name['BlockReply'] = _BLOCKREPLY

Strip = _reflection.GeneratedProtocolMessageType('Strip', (_message.Message,), dict(
  DESCRIPTOR = _STRIP,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:Strip)
  ))
_sym_db.RegisterMessage(Strip)

EncodeRequest = _reflection.GeneratedProtocolMessageType('EncodeRequest', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _ENCODEREQUEST_PARAMETERSENTRY,
    __module__ = 'playcloud_pb2'
    # @@protoc_insertion_point(class_scope:EncodeRequest.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _ENCODEREQUEST,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:EncodeRequest)
  ))
_sym_db.RegisterMessage(EncodeRequest)
_sym_db.RegisterMessage(EncodeRequest.ParametersEntry)

EncodeReply = _reflection.GeneratedProtocolMessageType('EncodeReply', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _ENCODEREPLY_PARAMETERSENTRY,
    __module__ = 'playcloud_pb2'
    # @@protoc_insertion_point(class_scope:EncodeReply.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _ENCODEREPLY,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:EncodeReply)
  ))
_sym_db.RegisterMessage(EncodeReply)
_sym_db.RegisterMessage(EncodeReply.ParametersEntry)

DecodeRequest = _reflection.GeneratedProtocolMessageType('DecodeRequest', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _DECODEREQUEST_PARAMETERSENTRY,
    __module__ = 'playcloud_pb2'
    # @@protoc_insertion_point(class_scope:DecodeRequest.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _DECODEREQUEST,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:DecodeRequest)
  ))
_sym_db.RegisterMessage(DecodeRequest)
_sym_db.RegisterMessage(DecodeRequest.ParametersEntry)

DecodeReply = _reflection.GeneratedProtocolMessageType('DecodeReply', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _DECODEREPLY_PARAMETERSENTRY,
    __module__ = 'playcloud_pb2'
    # @@protoc_insertion_point(class_scope:DecodeReply.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _DECODEREPLY,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:DecodeReply)
  ))
_sym_db.RegisterMessage(DecodeReply)
_sym_db.RegisterMessage(DecodeReply.ParametersEntry)

BlockRequest = _reflection.GeneratedProtocolMessageType('BlockRequest', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKREQUEST,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:BlockRequest)
  ))
_sym_db.RegisterMessage(BlockRequest)

BlockReply = _reflection.GeneratedProtocolMessageType('BlockReply', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKREPLY,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:BlockReply)
  ))
_sym_db.RegisterMessage(BlockReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\027ch.unine.iiun.safecloud')
_ENCODEREQUEST_PARAMETERSENTRY.has_options = True
_ENCODEREQUEST_PARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
_ENCODEREPLY_PARAMETERSENTRY.has_options = True
_ENCODEREPLY_PARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
_DECODEREQUEST_PARAMETERSENTRY.has_options = True
_DECODEREQUEST_PARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
_DECODEREPLY_PARAMETERSENTRY.has_options = True
_DECODEREPLY_PARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterEncoderDecoderServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Encode(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Decode(self, request, context):
    raise NotImplementedError()
class EarlyAdopterEncoderDecoderServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterEncoderDecoderStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Encode(self, request):
    raise NotImplementedError()
  Encode.async = None
  @abc.abstractmethod
  def Decode(self, request):
    raise NotImplementedError()
  Decode.async = None
def early_adopter_create_EncoderDecoder_server(servicer, port, private_key=None, certificate_chain=None):
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  method_service_descriptions = {
    "Decode": alpha_utilities.unary_unary_service_description(
      servicer.Decode,
      playcloud_pb2.DecodeRequest.FromString,
      playcloud_pb2.DecodeReply.SerializeToString,
    ),
    "Encode": alpha_utilities.unary_unary_service_description(
      servicer.Encode,
      playcloud_pb2.EncodeRequest.FromString,
      playcloud_pb2.EncodeReply.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("EncoderDecoder", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_EncoderDecoder_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  method_invocation_descriptions = {
    "Decode": alpha_utilities.unary_unary_invocation_description(
      playcloud_pb2.DecodeRequest.SerializeToString,
      playcloud_pb2.DecodeReply.FromString,
    ),
    "Encode": alpha_utilities.unary_unary_invocation_description(
      playcloud_pb2.EncodeRequest.SerializeToString,
      playcloud_pb2.EncodeReply.FromString,
    ),
  }
  return early_adopter_implementations.stub("EncoderDecoder", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaEncoderDecoderServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Encode(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Decode(self, request, context):
    raise NotImplementedError()

class BetaEncoderDecoderStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Encode(self, request, timeout):
    raise NotImplementedError()
  Encode.future = None
  @abc.abstractmethod
  def Decode(self, request, timeout):
    raise NotImplementedError()
  Decode.future = None

def beta_create_EncoderDecoder_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  request_deserializers = {
    ('EncoderDecoder', 'Decode'): playcloud_pb2.DecodeRequest.FromString,
    ('EncoderDecoder', 'Encode'): playcloud_pb2.EncodeRequest.FromString,
  }
  response_serializers = {
    ('EncoderDecoder', 'Decode'): playcloud_pb2.DecodeReply.SerializeToString,
    ('EncoderDecoder', 'Encode'): playcloud_pb2.EncodeReply.SerializeToString,
  }
  method_implementations = {
    ('EncoderDecoder', 'Decode'): face_utilities.unary_unary_inline(servicer.Decode),
    ('EncoderDecoder', 'Encode'): face_utilities.unary_unary_inline(servicer.Encode),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_EncoderDecoder_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  request_serializers = {
    ('EncoderDecoder', 'Decode'): playcloud_pb2.DecodeRequest.SerializeToString,
    ('EncoderDecoder', 'Encode'): playcloud_pb2.EncodeRequest.SerializeToString,
  }
  response_deserializers = {
    ('EncoderDecoder', 'Decode'): playcloud_pb2.DecodeReply.FromString,
    ('EncoderDecoder', 'Encode'): playcloud_pb2.EncodeReply.FromString,
  }
  cardinalities = {
    'Decode': cardinality.Cardinality.UNARY_UNARY,
    'Encode': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'EncoderDecoder', cardinalities, options=stub_options)
class EarlyAdopterProxyServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetRandomBlocks(self, request, context):
    raise NotImplementedError()
class EarlyAdopterProxyServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterProxyStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetRandomBlocks(self, request):
    raise NotImplementedError()
  GetRandomBlocks.async = None
def early_adopter_create_Proxy_server(servicer, port, private_key=None, certificate_chain=None):
  import playcloud_pb2
  import playcloud_pb2
  method_service_descriptions = {
    "GetRandomBlocks": alpha_utilities.unary_unary_service_description(
      servicer.GetRandomBlocks,
      playcloud_pb2.BlockRequest.FromString,
      playcloud_pb2.BlockReply.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("Proxy", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_Proxy_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import playcloud_pb2
  import playcloud_pb2
  method_invocation_descriptions = {
    "GetRandomBlocks": alpha_utilities.unary_unary_invocation_description(
      playcloud_pb2.BlockRequest.SerializeToString,
      playcloud_pb2.BlockReply.FromString,
    ),
  }
  return early_adopter_implementations.stub("Proxy", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaProxyServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetRandomBlocks(self, request, context):
    raise NotImplementedError()

class BetaProxyStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetRandomBlocks(self, request, timeout):
    raise NotImplementedError()
  GetRandomBlocks.future = None

def beta_create_Proxy_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import playcloud_pb2
  import playcloud_pb2
  request_deserializers = {
    ('Proxy', 'GetRandomBlocks'): playcloud_pb2.BlockRequest.FromString,
  }
  response_serializers = {
    ('Proxy', 'GetRandomBlocks'): playcloud_pb2.BlockReply.SerializeToString,
  }
  method_implementations = {
    ('Proxy', 'GetRandomBlocks'): face_utilities.unary_unary_inline(servicer.GetRandomBlocks),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_Proxy_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import playcloud_pb2
  import playcloud_pb2
  request_serializers = {
    ('Proxy', 'GetRandomBlocks'): playcloud_pb2.BlockRequest.SerializeToString,
  }
  response_deserializers = {
    ('Proxy', 'GetRandomBlocks'): playcloud_pb2.BlockReply.FromString,
  }
  cardinalities = {
    'GetRandomBlocks': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'Proxy', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)