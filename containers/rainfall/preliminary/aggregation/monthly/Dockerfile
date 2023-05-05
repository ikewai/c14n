# Start with the Rainfall Preliminary Aggregation Base.
FROM ghcr.io/ikewai/task-rf-pre-agg-base:latest
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n/containers/rainfall/preliminary/aggregation/monthly"
LABEL org.opencontainers.image.description="Monthly Rainfall Aggregation."

# Make directories for script and data file placement. The directory list is specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/rainfall/main/docs/monthly/currentDirs.txt -O /build/currentDirs.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Get workflow scripts. The lists of scripts are provided by this repo, and they point to the workflow code repo.
ADD /containers/rainfall/preliminary/aggregation/monthly/data/r_script_list.json /build/r_script_list.json
ADD /containers/rainfall/preliminary/aggregation/monthly/data/r_module_list.json /build/r_module_list.json
ADD /containers/rainfall/preliminary/aggregation/monthly/data/sh_script_list.json /build/sh_script_list.json
RUN python3 /build/wget_from_json.py /build/r_script_list.json
RUN python3 /build/wget_from_json.py /build/r_module_list.json
RUN python3 /build/wget_from_json.py /build/sh_script_list.json

# Get the container's upload config as specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/rainfall/main/upload_configs/intermediate_products.json -O /sync/intermediate_products.json
RUN wget https://raw.githubusercontent.com/ikewai/rainfall/main/upload_configs/final_products.json -O /sync/final_products.json

# Copy in the task script.
ADD /containers/rainfall/preliminary/aggregation/monthly/scripts/task.sh /actor/task.sh

# This container is intended to run the task wrapper at launch, unless otherwise specified at run-time.
CMD [ "/bin/bash", "/actor/task.sh" ]