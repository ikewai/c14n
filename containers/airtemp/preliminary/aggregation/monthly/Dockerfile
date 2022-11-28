FROM ikewai/task-at-pre-agg-base

# Make directories
ADD /tools/build-tools/airtemp-specific/mkdir_from_txt_monthlyagg.py /build/mkdir_from_txt_monthlyagg.py
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/monthly/docs/currentDirs.txt -O /build/currentDirs.txt
RUN /bin/python3 /build/mkdir_from_txt_monthlyagg.py /build/currentDirs.txt

# Get scripts
ADD /containers/airtemp/preliminary/aggregation/monthly/data/py_script_list.json /build/py_script_list.json
RUN python3 /build/wget_from_json.py /build/py_script_list.json

# Get upload config
WORKDIR /sync
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/monthly/docs/upload_config.json

ADD /containers/airtemp/preliminary/aggregation/monthly/scripts/task.sh /actor/task.sh

CMD [ "/bin/bash", "/actor/task.sh" ]