# Start with the Air Temperature Preliminary Aggregation Base.
FROM ghcr.io/ikewai/task-at-pre-agg-base:latest
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n"
LABEL org.opencontainers.image.description="Monthly Air Temperature Aggregation and Mapping."

# Make directories for script and data file placement.
# Directories for daily scripts/data
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/daily/docs/currentDirs.txt -O /build/currentDirs_daily.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs_daily.txt
# Directories for monthly scripts/data. Also uses a modified version of the directory maker to match the directory list's file format.
ADD /tools/build-tools/airtemp-specific/mkdir_from_txt_monthlyagg.py /build/mkdir_from_txt_monthlyagg.py
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/monthly/docs/currentDirs.txt -O /build/currentDirs.txt
RUN /bin/python3 /build/mkdir_from_txt_monthlyagg.py /build/currentDirs.txt

# Get workflow scripts. The list of scripts is provided by this repo, and points to the workflow code repo.
ADD /containers/airtemp/preliminary/aggregation/monthly/data/py_script_list.json /build/py_script_list.json
RUN python3 /build/wget_from_json.py /build/py_script_list.json

# Get the container's upload config as specified in the code repo.
WORKDIR /sync
RUN wget https://raw.githubusercontent.com/ikewai/airtemp/main/monthly/docs/upload_config.json

# Add the task wrapper script.
ADD /containers/airtemp/preliminary/aggregation/monthly/scripts/task.sh /actor/task.sh

# This container is intended to run the task wrapper at launch, unless otherwise specified at run-time.
CMD [ "/bin/bash", "/actor/task.sh" ]