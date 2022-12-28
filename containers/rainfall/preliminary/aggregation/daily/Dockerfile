# Start with the Rainfall Preliminary Aggregation Base.
FROM ikewai/task-rf-pre-agg-base

# Make directories for script and data file placement. The directory list is specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/daily/currentDirs.txt -O /build/currentDirs.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Get workflow scripts. The list of scripts is provided by this repo, and points to the workflow code repo.
ADD /containers/rainfall/preliminary/aggregation/daily/data/r_script_list.json /build/r_script_list.json
RUN python3 /build/wget_from_json.py /build/r_script_list.json

# Shim the scripts with jetpack. This is necessary to make the scripts compatible with the agg-base container's build strategy.
RUN sed -i '1 s/^/jetpack::load()\n/' /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/*.R

# Get the container's upload config as specified in the workflow code repo.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/daily/upload_config.json -O /sync/upload_config.json

# Copy in the task wrapper script.
ADD /containers/rainfall/preliminary/aggregation/daily/scripts/task.sh /actor/task.sh

# This container is intended to run the task wrapper at launch, unless otherwise specified at run-time.
CMD [ "/bin/bash", "/actor/task.sh" ]