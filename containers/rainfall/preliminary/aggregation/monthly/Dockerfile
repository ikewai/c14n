# Start with the Rainfall Preliminary Aggregation Base.
FROM ikewai/task-rf-pre-agg-base

# Make directories for script and data file placement. The directory list is specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/monthly/currentDirs.txt -O /build/currentDirs.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Get workflow scripts. The lists of scripts are provided by this repo, and they point to the workflow code repo.
ADD /containers/rainfall/preliminary/aggregation/monthly/data/r_script_list.json /build/r_script_list.json
ADD /containers/rainfall/preliminary/aggregation/monthly/data/sh_script_list.json /build/sh_script_list.json
RUN python3 /build/wget_from_json.py /build/r_script_list.json
RUN python3 /build/wget_from_json.py /build/sh_script_list.json

# Get the container's upload config as specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/monthly/upload_config.json -O /sync/upload_config.json

# Copy in the task script.
ADD /containers/rainfall/preliminary/aggregation/monthly/scripts/task.sh /actor/task.sh

# This container is intended to run the task wrapper at launch, unless otherwise specified at run-time.
CMD [ "/bin/bash", "/actor/task.sh" ]