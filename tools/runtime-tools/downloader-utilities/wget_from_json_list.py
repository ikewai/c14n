#!/bin/python3

# This script runs the `wget` command with input URLs and output names and directories.
# Arg 1: JSON list containing the following in each element:
# "url": The full URL of the file to download
# "name" The name to give the file when it's downloaded.

import json
import sys
import subprocess

# Load the JSON list of files to download from the first command line argument
with open(sys.argv[1], 'rt') as fin:
    file_list = json.loads(fin.read())

# Download each file in the list using the `wget` command
for file in file_list:
    subprocess.run(["/bin/bash", "-c", f"wget {file['url']} -O {file['name']}"])