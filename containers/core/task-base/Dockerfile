# Starting with Ubuntu 20.04 as the base image.
# Supported with hardware and maintenance updates until Q3 2024.
FROM ubuntu:20.04
#TODO update to 22.04 (exp Q3 2026)

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update

# Install Python and its native package manager, Pip.
# For running Tapis' Python SDKs, as well as any Python-based workflows.
RUN apt install -y python3 python3-pip

# Install wget.
# For acquiring files from web sources, such as github repos and science gateways.
RUN apt install -y wget

# Install git.
# For pulling and interacting with repositories.
RUN apt install -y git

# Install the Tapipy and Agavepy SDKs.
# For interacting with Tapis v3 and v2, respectively.
RUN python3 -m pip install tapipy agavepy


## FILE ADDITIONS ##
# Add build manifest generator
ADD /tools/tagging-tools/make_build_manifest.py /tools/tagging-tools/make_build_manifest.py


## OPERATIONS ##
# Create the build's manifest.
ADD /containers/core/task-base/repos.json /build/repos.json
RUN python3 /tools/tagging-tools/make_build_manifest.py /build/repos.json /build/manifest.json