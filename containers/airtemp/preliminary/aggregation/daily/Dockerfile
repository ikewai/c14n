# Start with the Air Temperature Preliminary Aggregation Base.
FROM ghcr.io/ikewai/task-at-pre-agg-base:latest

# Make directories for script and data file placement. The directory list is specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/daily/docs/currentDirs.txt -O /build/currentDirs.txt
RUN /bin/python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Get workflow scripts. The list of scripts is provided by this repo, and points to the workflow code repo.
ADD /containers/airtemp/preliminary/aggregation/daily/data/py_script_list.json /build/py_script_list.json
RUN python3 /build/wget_from_json.py /build/py_script_list.json

# Get the container's upload config as specified in the code repo.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/daily/docs/upload_config.json -O /sync/upload_config.json

# Add the task wrapper script.
ADD /containers/airtemp/preliminary/aggregation/daily/scripts/task.sh /actor/task.sh

# This container is intended to run the task wrapper at launch, unless otherwise specified at run-time.
CMD [ "/bin/bash", "/actor/task.sh" ]