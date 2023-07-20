FROM ghcr.io/ikewai/task-sh-aq-base:latest

# Get the R dependencies.
RUN R -e "install.packages('plyr')"

# Get the scripts.
ADD /containers/shared/acquisition/nws-daily/data/files_to_acquire.json /build/files_to_acquire.json
RUN python3 /tools/build-tools/wget_from_json.py /build/files_to_acquire.json

# Copy the upload configuration.
ADD /containers/shared/acquisition/nws-daily/data/upload_config.json /sync/upload_config.json

# Copy the task definition script.
ADD /containers/shared/acquisition/nws-daily/scripts/task.sh /actor/task.sh

CMD [ "/bin/bash", "/actor/task.sh" ]