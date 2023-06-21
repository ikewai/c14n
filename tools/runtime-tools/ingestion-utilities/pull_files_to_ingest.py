#!/usr/bin/env python3
# Pulls the files specified by the download section of an ingestion config.

import json
import sys
import subprocess

# Load the config file specified as the first command line argument
fname = str(sys.argv[1])
with open(fname, "rt") as config_file:
    config_dict: dict = json.loads(config_file.read())

# Extract the base URL and list of files to download from the config
base_url = config_dict["download_base_url"]
files_to_download = config_dict["download"]

# Download each file using wget
for file in files_to_download:
    wget_cmd: str = f"wget -P /ingest {base_url}{file}"
    subprocess.run(["/bin/bash", "-c", wget_cmd])