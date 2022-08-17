FROM ikewai/task-rf-pre-agg-base

# Get the dir list for daily agg, then create all the directories.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/monthly/currentDirs.txt -O /build/currentDirs.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs.txt

ADD /containers/rainfall/preliminary/aggregation/monthly/data/r_script_list.json /build/r_script_list.json
ADD /containers/rainfall/preliminary/aggregation/monthly/data/sh_script_list.json /build/sh_script_list.json
RUN python3 /build/wget_from_json.py /build/r_script_list.json
RUN python3 /build/wget_from_json.py /build/sh_script_list.json

ADD /containers/rainfall/preliminary/aggregation/monthly/scripts/task.sh /actor/task.sh

CMD [ "/root/anaconda3/bin/conda", "run", "--no-capture-output", "-n", "container_env", "/bin/bash", "/actor/task.sh" ]