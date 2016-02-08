#! /bin/bash
###############################################################################
# microbench.sh                                                               #
#                                                                             #
# Benchmarks a GRPC enabled encoder/decoder implementing the behaviour        #
# defined in playclcoud.proto.                                                #
###############################################################################

source ./utils.sh

function print_usage {
	echo -e "Usage: ${0} <env-file> <repetitions>\n"
	echo -e "Arguments:"
	echo -e "\tenv-file           Environment file containing the values that should be used by the encoder/decoder"
	echo -e "\trepetitions        Number of repetitions"
}

if [[ "${#}" -ne 2 ]]; then
	print_usage
	exit 0
fi

ENV_FILE="${1}"
ENV_FILE_CONTENT="$(cat "${ENV_FILE}")"
REPETITIONS="${2}"
source "${ENV_FILE}"
DATA_DIRECTORY="xpdata/pyeclib/$(basename "${EC_TYPE}")/"
declare -a SIZES=("4" "16" "64")

cd microbencher
docker build -t pyeclib-microbencher -f pyeclib.Dockerfile .
cd -
mkdir -p "${DATA_DIRECTORY}"


for size in "${SIZES[@]}"; do
	ADJUSTED_SIZE="$((size * 1024 * 1024))"
	for rep in $(seq "${REPETITIONS}"); do
		docker run -it --rm -v "${PWD}/xpdata/pyeclib":/opt/xpdata/pyeclib pyeclib-microbencher \
                bash -c "eval ${ENV_FILE_CONTENT} && /usr/local/src/app/microbench_local_encode.py ${ADJUSTED_SIZE} > /opt/$DATA_DIRECTORY/microbench-encode-${size}MB-${rep}.dat"
	done
done
