FROM ghcr.io/ikewai/task-rf-pre-base:latest
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n"
LABEL org.opencontainers.image.description="Base Image for preliminary rainfall aggregation workflows."

# Install a data package that allows for easily setting time zones in a shell script.
RUN apt install -y tzdata

RUN mkdir /sync
ADD /tools/runtime-tools/uploader-utilities/* /sync/

RUN wget https://raw.githubusercontent.com/ikewai/data-uploader/main/upload.py -O /sync/upload.py