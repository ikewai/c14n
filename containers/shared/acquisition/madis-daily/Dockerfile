FROM ikewai/task-sh-aq-base

# Copy the upload configuration.
ADD /containers/shared/acquisition/madis-daily/data/upload_config.json /sync/config.json

# Copy the task definition script.
ADD /containers/shared/acquisition/madis-daily/scripts/task.sh /actor/.

CMD [ "/bin/bash", "/actor/task.sh" ]