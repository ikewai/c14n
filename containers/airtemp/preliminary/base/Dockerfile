FROM ikewai/task-base

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update
# Let APT know that we don't have a terminal.
ENV DEBIAN_FRONTEND=noninteractive

# Install libgdal.
# This is experimental - The scripts had some
# issues with newer versions of gdal during previous c14n.
RUN apt install -y libgdal-dev

# Install dependencies for the air temp workflows.
# Specific explanations of each library coming soon.
# Libraries are approximately ordered by dependency,
# then by time-to-install.
RUN python3 -m pip install numpy==1.21.2
RUN python3 -m pip install scipy==1.7.3
RUN python3 -m pip install gdal==$(gdal-config --version)
RUN python3 -m pip install rasterio
RUN python3 -m pip install matplotlib==3.5.0
RUN python3 -m pip install pandas==1.3.5
RUN python3 -m pip install affine==2.3.0
RUN python3 -m pip install pyproj==3.0.1
RUN python3 -m pip install statsmodels==0.13.0
RUN python3 -m pip install scikit-learn
RUN python3 -m pip install tiffile
RUN python3 -m pip install python-dotenv
RUN python3 -m pip install pathlib
RUN python3 -m pip install xarray==0.20.1

# Bring in the airtemp-specific script for making directories.
ADD /tools/build-tools/airtemp-specific/mkdir_from_txt.py /build/mkdir_from_txt.py

# Bring in the script acquirer.
ADD /tools/build-tools/wget_from_json.py /build/wget_from_json.py
