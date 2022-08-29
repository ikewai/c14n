FROM ikewai/task-base

# Bring in the script acquirer.
ADD /tools/build-tools/wget_from_json.py /build/.

# Copy the lists of files.
ADD /containers/ingestion/data/station_metadata_file_list.json /build/.
ADD /containers/ingestion/data/station_values_file_list.json /build/.


# Pull code for station metadata ingestion
RUN /bin/python3 /build/wget_from_json.py /build/station_metadata_file_list.json
# Pull code for station value ingestion
RUN /bin/python3 /build/wget_from_json.py /build/station_values_file_list.json