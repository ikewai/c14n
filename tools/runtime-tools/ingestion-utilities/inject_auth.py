#!/bin/python3
# This script applies a value from the environment to the "token" key in the given json file.

# Usage: python3 inject_auth.py TOKEN_KEY config.json
# Arg 1: Name of the environment variable containing the token.
# Arg 2: Path of the JSON file to inject the token into.

import os # For accessing environment variables.
import sys # For accessing execution args.
from io import TextIOWrapper # For hinting type in file read/writes
import json # For interacting with JSON data.


# Get token from environment variable.
auth_token_env_key: str = str(sys.argv[1])
auth_token: str = str(os.environ[auth_token_env_key])

# Get configuration dict from json file.
fin: TextIOWrapper = open(sys.argv[2], "rt")
fin_string: str = str(fin.read())
fin.close()
config_json: dict = json.loads(fin_string)

# Set auth token in dict.
config_json['tapis_config']['token']: str = auth_token

# Convert dict to JSON-formatted string.
config_str: str = json.dumps(config_json)

# Write updated config to disk.
fout: TextIOWrapper = open(sys.argv[2], "wt")
fout.write(config_str)
fout.close()

# Done.