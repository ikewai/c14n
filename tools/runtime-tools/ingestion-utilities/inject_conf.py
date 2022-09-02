#!/bin/python3
# This script injects configuration data from JSON-formatted strings
# in the environment into the "data" field of the given config file.

import os # For accessing environment variables.
import sys # For accessing execution args.
from io import TextIOWrapper # For hinting type in file read/writes.
import json # For interacting with JSON data.

# Get configuration JSON from environment variable. 
config_env_key: str = str(sys.argv[1])
config_env: str = str(os.environ[config_env_key])
config_env: dict = json.loads(config_env)

# Get configuration dict from json file.
fin: TextIOWrapper = open(sys.argv[2], "rt")
fin_string: str = str(fin.read())
fin.close()
config_json: dict = json.loads(fin_string)

# Set data values from environment variable.
config_json['data'] = config_env['data']

# Convert output dict to JSON-formatted string.
config_str: str = json.dumps(config_json)

# Write updated config to disk.
fout: TextIOWrapper = open(sys.argv[2], "wt")
fout.write(config_str)
fout.close()

# Done.