FROM ikewai/task-at-pre-agg-base

# Make directories
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/daily/docs/currentDirs.txt -O /build/currentDirs.txt
RUN /bin/python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Get scripts
ADD /containers/airtemp/preliminary/aggregation/daily/data/py_script_list.json /build/py_script_list.json
RUN python3 /build/wget_from_json.py /build/py_script_list.json

ADD /containers/airtemp/preliminary/aggregation/daily/scripts/task.sh /actor/task.sh

CMD [ "/bin/bash", "/actor/task.sh" ]