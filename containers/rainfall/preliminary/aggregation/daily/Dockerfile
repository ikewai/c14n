FROM ikewai/task-rf-pre-agg-base

# Get the dir list for daily agg, then create all the directories.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/daily/currentDirs.txt -O /build/currentDirs.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Add the lists of workflow scripts for the container.
ADD /containers/rainfall/preliminary/aggregation/daily/data/r_script_list.json /build/r_script_list.json

# Get the workflow scripts.
RUN python3 /build/wget_from_json.py /build/r_script_list.json

# Shim the scripts with jetpack.
RUN sed -i '1 s/^/jetpack::load()\n/' /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/*.R

# Download the uploader configuration.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/daily/upload_config.json -O /sync/upload_config.json

# Copy in the task script.
ADD /containers/rainfall/preliminary/aggregation/daily/scripts/task.sh /actor/task.sh

CMD [ "/bin/bash", "/actor/task.sh" ]