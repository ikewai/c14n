FROM ghcr.io/ikewai/task-rf-pre-base:latest

RUN mkdir /sync
ADD /tools/runtime-tools/uploader-utilities/* /sync/

RUN wget https://raw.githubusercontent.com/ikewai/data-uploader/main/upload.py -O /sync/upload.py