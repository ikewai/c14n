FROM ikewai/task-at-pre-agg-base

# Make directories
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/daily/docs/currentDirs.txt -O /build/currentDirs.txt
RUN /bin/python3 /build/mkdir_from_txt.py /build/currentDirs.txt

# Get scripts
ADD /containers/airtemp/preliminary/aggregation/daily/data/py_script_list.json /build/py_script_list.json
RUN /build/wget_from_json.py /build/py_script_list.json

# Add and chmod task.sh (chmod is temporary, for dev purposes)
ADD /containers/airtemp/preliminary/aggregation/daily/scripts/task.sh /actor/task.sh
RUN chmod +x /actor/task.sh