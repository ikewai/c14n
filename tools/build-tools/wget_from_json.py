#!/bin/python3

# This script downloads files specified in a JSON-formatted dictionary.
# The dictionary must contain the following:
#   "remote_url": str - An absolute base URL that all of the downloads include.
#   "local_dir": str - An absolute placement directory to download the files to.
#   "files": list(str) - A list of files to download.

# Requires wget to be installed.

import sys # For reading the execution argument(s).
import json # For reading the JSON-formatted dict.
import subprocess # For executing wget.


# Check for arguments
if (sys.argv[1] == None) or (str(sys.argv[1]) == "") or not (str(sys.argv[1].__contains__(".json"))):
    print("This script needs args! Pass it a json manifest.")
    exit(1)

# Take arg 1 as the json file to read, then load the file.
fname = str(sys.argv[1])
with open(fname, "rt") as json_file:
    json_file_dict: dict = json.loads(json_file.read())

# Set variables from the loaded file/dict.
remote_url: str = json_file_dict["base_url"]
local_dir: str = json_file_dict["local_dir"]
files: list = json_file_dict["files"]

# Download the files.
for file in files:
    command: str = f"wget {remote_url}{file} -O {local_dir}{file}"
    subprocess.run(["/bin/bash", "-c", command])