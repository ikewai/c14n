FROM ikewai/task-rf-pre-agg-base

# Get the dir list for daily agg, then create all the directories.
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/monthly/currentDirs.txt -O /build/currentDirs.txt
RUN python3 /build/mkdir_from_txt.py /build/currentDirs.txt

ADD /containers/rainfall/preliminary/aggregation/daily/scripts/task.sh /actor/task.sh

CMD [ "/bin/bash", "/actor/task.sh" ]