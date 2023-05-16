FROM ghcr.io/ikewai/task-base:latest
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n"
LABEL org.opencontainers.image.description="Base Image for data acquisition containers."

# Add pytz dependency (madis)
RUN python3 -m pip install pytz
# Add pandas dependency (madis)
RUN python3 -m pip install pandas
# Add xarray dependency (madis)
RUN python3 -m pip install xarray netcdf4 scipy

# Add R (nws, hads)
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y r-base

## FILE COPIES/DOWNLOADS ##
# Copy build tools for creating directories and pulling scripts at build-time.
RUN mkdir /build
ADD /tools/build-tools/acquisition-specific/mkdir_from_txt.py /tools/build-tools/mkdir_from_txt.py
ADD /tools/build-tools/wget_from_json.py /tools/build-tools/wget_from_json.py
RUN wget https://raw.githubusercontent.com/ikewai/data_aqs/main/docs/currentDirs.txt -O /build/currentDirs.txt

# Pull the latest version of the data uploader.
RUN mkdir /sync
RUN wget https://raw.githubusercontent.com/ikewai/data-uploader/main/upload.py -O /sync/upload.py

# Copy the upload support utilities.
ADD /tools/runtime-tools/uploader-utilities/add_auth_info_to_config.py /sync/add_auth_info_to_config.py
ADD /tools/runtime-tools/uploader-utilities/add_upload_list_to_config.py /sync/add_upload_list_to_config.py
ADD /tools/runtime-tools/uploader-utilities/update_date_string_in_config.py /sync/update_date_string_in_config.py

## OPERATIONS ##
# Create directories and pull scripts for acquisition.
RUN python3 /tools/build-tools/mkdir_from_txt.py /build/currentDirs.txt
