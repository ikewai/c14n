FROM ghcr.io/ikewai/task-base:latest
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n"
LABEL org.opencontainers.image.description="Base Image for preliminary air temperature workflows."

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update
# Let APT know that we don't have a terminal.
ENV DEBIAN_FRONTEND=noninteractive

# Install libgdal.
# This is experimental - The scripts had some
# issues with newer versions of gdal during previous c14n.
RUN apt install -y libgdal-dev

# Install a data package that allows for easily setting time zones in a shell script.
RUN apt install -y tzdata

# Install dependencies for the air temp workflows.
# Specific explanations of each library coming soon.
# Libraries are approximately ordered by dependency,
# then by time-to-install.
RUN python3 -m pip install numpy
RUN python3 -m pip install scipy
RUN python3 -m pip install gdal==$(gdal-config --version)
RUN python3 -m pip install rasterio
RUN python3 -m pip install matplotlib
RUN python3 -m pip install pandas
RUN python3 -m pip install affine
RUN python3 -m pip install pyproj==3.3.0
RUN python3 -m pip install statsmodels
RUN python3 -m pip install scikit-learn
RUN python3 -m pip install tiffile
RUN python3 -m pip install python-dotenv
RUN python3 -m pip install pathlib
RUN python3 -m pip install xarray

# Bring in the airtemp-specific script for making directories.
ADD /tools/build-tools/airtemp-specific/mkdir_from_txt.py /build/mkdir_from_txt.py

# Bring in the script acquirer.
ADD /tools/build-tools/wget_from_json.py /build/wget_from_json.py
