FROM ikewai/task-rf-pre-agg-base

# Get the dir list for daily agg, then create all the directories.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/daily/currentDirs.txt -O /build/currentDirs.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Add the lists of workflow scripts for the container.
ADD /containers/rainfall/preliminary/aggregation/daily/data/r_script_list.json /build/r_script_list.json
ADD /containers/rainfall/preliminary/aggregation/daily/data/sh_script_list.json /build/sh_script_list.json

# Get the workflow scripts.
RUN python3 /build/wget_from_json.py /build/r_script_list.json
RUN python3 /build/wget_from_json.py /build/sh_script_list.json

ADD /containers/rainfall/preliminary/aggregation/daily/scripts/task.sh /actor/task.sh

CMD [ "/root/miniconda3/bin/conda", "run", "--no-capture-output", "-n", "container_env", "/bin/bash", "/actor/task.sh" ]