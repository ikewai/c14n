FROM ikewai/task-at-pre-base

RUN mkdir -p /sync
RUN wget https://raw.githubusercontent.com/ikewai/data-uploader/main/upload.py -O /sync/upload.py

ADD /tools/runtime-tools/uploader-utilities/* /sync/