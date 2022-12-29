FROM ikewai/task-base

# Install curl, prerequisite for get_auth_token.py.
RUN apt install -y curl

# Bring in the script acquirer.
ADD /tools/build-tools/wget_from_json.py /build/wget_from_json.py

# Copy in the config datestring updater.
ADD /tools/runtime-tools/uploader-utilities/update_date_string_in_config.py /actor/update_date_string_in_config.py

# Copy the lists of files.
ADD /containers/ingestion/station_metadata/data/station_metadata_file_list.json /build/.
ADD /containers/ingestion/station_values/data/station_values_file_list.json /build/.
ADD /containers/ingestion/station_metadata/data/station_metadata_python_modules.json /build/.
ADD /containers/ingestion/station_values/data/station_values_python_modules.json /build/.

# Make directories for scripts
RUN mkdir -p /home/hcdp_tapis_ingestor/station_metadata/
RUN mkdir -p /home/hcdp_tapis_ingestor/station_values/
# Pull code for station metadata ingestion
RUN /bin/python3 /build/wget_from_json.py /build/station_metadata_file_list.json
RUN /bin/python3 /build/wget_from_json.py /build/station_metadata_python_modules.json
# Pull code for station value ingestion
RUN /bin/python3 /build/wget_from_json.py /build/station_values_file_list.json
RUN /bin/python3 /build/wget_from_json.py /build/station_values_python_modules.json

# Copy the file downloader
ADD /tools/runtime-tools/ingestion-utilities/pull_files_to_ingest.py /actor/pull_files_to_ingest.py

# Copy the ingestion utilities
ADD /tools/runtime-tools/ingestion-utilities/inject_auth.py /actor/inject_auth.py
ADD /tools/runtime-tools/ingestion-utilities/get_auth_token.py /actor/get_auth_token.py

ADD /containers/ingestion/station_metadata/scripts/task.sh /actor/task.sh

CMD [ "/bin/bash", "/actor/task.sh" ]
