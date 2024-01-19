# Starting with Ubuntu 22.04 as the base image.
# Supported with hardware and maintenance updates until Q3 2026.
FROM ubuntu:22.04
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n"
LABEL org.opencontainers.image.description="Base Image for containerized workflows. Python, wget, git, and tapipy+agavepy."

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update

# Install Python and its native package manager, Pip.
# For running Tapis' Python SDKs, as well as any Python-based workflows.
RUN apt install -y python3 python3-pip

# pip 22.0.2 is broken.
RUN python3 -m pip install pip==22.0.3

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
RUN apt install -y software-properties-common
RUN apt update
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install -y python3.8
RUN echo "alias python3.8=/usr/bin/python3.8" >> /etc/profile.d/python3.8-alias.sh

# Install wget.
# For acquiring files from web sources, such as github repos and science gateways.
RUN apt install -y wget

# Install git.
# For pulling and interacting with repositories.
RUN apt install -y git

# Install nano.
# For debugging and working directly in a container.
RUN apt install -y nano

# Install the Tapipy and Agavepy SDKs.
# For interacting with Tapis v3 and v2, respectively.
RUN python3 -m pip install tapipy agavepy
