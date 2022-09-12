FROM ikewai/task-base

## FILE COPIES/DOWNLOADS ##
# Copy build tools for creating directories and pulling scripts at build-time.
ADD /tools/build-tools/mkdir_from_json.py /tools/build-tools/mkdir_from_json.py
ADD /tools/build-tools/wget_from_json.py /tools/build-tools/wget_from_json.py
ADD /containers/shared/acquisition/base/data/directories_to_create.json /build/.
ADD /containers/shared/acquisition/base/data/files_to_acquire.json /build/.

# Pull the latest version of the data uploader.
RUN wget https://raw.githubusercontent.com/ikewai/data-uploader/main/upload.py -O /sync/upload.py

# Copy the upload support utilities.
ADD /tools/runtime-tools/uploader-utilites/* /sync/.

## OPERATIONS ##
# Create directories and pull scripts for acquisition.
RUN python3 /tools/build-tools/mkdir_from_json.py /build/directories_to_create.json
RUN python3 /tools/build-tools/wget_from_json.py /build/files_to_acquire.json

# Create the build's manifest.
ADD /containers/shared/acquisition/base/repos.json /build/repos.json
RUN python3 /tools/tagging-tools/make_build_manifest.py /build/repos.json /build/manifest.json