# This script deletes a batch of files using the agavepy library.
# It takes in a file containing a JSON list of remote file paths to delete.

# The JSON file should be formatted as follows:
# {
#   "api_server": "https://ikeauth.its.hawaii.edu",
#   "systemId": "ikewai-annotated-data",
#   "filePathList": [
#       "/path/to/file1",
#       "/path/to/file2",
#       ...
#   ]
# }

import argparse
import json
import os
from agavepy import Agave


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", help="JSON file containing file paths to delete")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Perform a dry run without actually deleting the files")
    args = parser.parse_args()

    # Read in the JSON file
    with open(args.json_file, "r") as f:
        json_data = json.load(f)

    # Get the file paths to delete
    file_path_list = json_data["filePathList"]

    # Get the Agave API server
    api_server = json_data["api_server"]

    # Get the system ID
    system_id = json_data["systemId"]

    # Initialize the Agave client
    ag = Agave(api_server=api_server,
                username=os.environ['IW_USERNAME'],
                password=os.environ['IW_PASSWORD'],
                api_key=os.environ['IW_API_KEY'],
                api_secret=os.environ['IW_API_SECRET'],)
    
    # Delete the files
    for file_path in file_path_list:
        if args.dry_run:
            print("Would delete file: {}".format(file_path))
        else:
            print("Deleting file: {}".format(file_path))
            ag.files.delete(systemId=system_id, filePath=file_path)


if __name__ == "__main__":
    main()