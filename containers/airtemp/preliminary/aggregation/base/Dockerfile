FROM ghcr.io/ikewai/task-at-pre-base:latest
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n"
LABEL org.opencontainers.image.description="Base Image for preliminary air temperature aggregation."

RUN mkdir -p /sync
RUN wget https://raw.githubusercontent.com/ikewai/data-uploader/main/upload.py -O /sync/upload.py

ADD /tools/runtime-tools/uploader-utilities/* /sync/