# Start with the Rainfall Preliminary Aggregation Base.
FROM ghcr.io/ikewai/task-rf-pre-agg-base:latest
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n/rainfall/preliminary/aggegation/daily"
LABEL org.opencontainers.image.description="Daily Rainfall Aggregation."

# Make directories for script and data file placement. The directory list is specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/daily/currentDirs.txt -O /build/currentDirs.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Pull the daily dependencies and extract them.
WORKDIR /home/hawaii_climate_products_container/preliminary/rainfall/dependencies
RUN wget -nv https://ikeauth.its.hawaii.edu/files/v2/download/public/system/ikewai-annotated-data/HCDP/workflow_data/preliminary/rainfall/dependencies/daily_dependencies.tar.gz
RUN tar -xf daily_dependencies.tar.gz
RUN rm daily_dependencies.tar.gz

# Get workflow scripts. The list of scripts is provided by this repo, and points to the workflow code repo.
ADD /containers/rainfall/preliminary/aggregation/daily/data/r_script_list.json /build/r_script_list.json
RUN python3 /build/wget_from_json.py /build/r_script_list.json
ADD /containers/rainfall/preliminary/aggregation/daily/data/daily_wget.json /build/daily_wget.json
RUN python3 /build/wget_from_json.py /build/daily_wget.json
ADD /containers/rainfall/preliminary/aggregation/daily/data/r_module_list.json /build/r_module_list.json
RUN python3 /build/wget_from_json.py /build/r_module_list.json

# Get the container's upload config as specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/rainfall/main/upload_configs/daily/final_products.json -O /sync/upload_config.json
RUN wget https://raw.githubusercontent.com/ikewai/rainfall/main/upload_configs/daily/intermediate_products.json -O /sync/intermediate_upload_config.json




# Copy in the task wrapper script.
ADD /containers/rainfall/preliminary/aggregation/daily/scripts/task.sh /actor/task.sh

# This container is intended to run the task wrapper at launch, unless otherwise specified at run-time.
CMD [ "/bin/bash", "/actor/task.sh" ]