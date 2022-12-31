# Starting with Ubuntu 22.04 as the base image.
# Supported with hardware and maintenance updates until Q3 2026.
FROM ubuntu:22.04

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