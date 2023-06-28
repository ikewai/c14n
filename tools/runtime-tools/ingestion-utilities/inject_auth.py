#!/bin/python3
# This script applies a value from a given text file to the "token" key in the given json file.

# Usage: python3 inject_auth.py token.txt config.json
# Arg 1: Path of the plaintext file containing the token.
# Arg 2: Path of the JSON file to inject the token into.

import os # For accessing environment variables.
import sys # For accessing execution args.
import json # For interacting with JSON data.


# Get token from environment variable.
token_fname: str = str(sys.argv[1])
auth_token_file = open(token_fname, "rt")
auth_token = auth_token_file.read()
auth_token_file.close()

# Get configuration dict from json file.
fin = open(sys.argv[2], "rt")
fin_string: str = str(fin.read())
fin.close()
config_json: dict = json.loads(fin_string)

# Set auth token in dict.
config_json['tapis_config']['token'] = auth_token

# Convert output dict to JSON-formatted string.
config_str: str = json.dumps(config_json)

# Write updated config to disk.
fout = open(sys.argv[2], "wt")
fout.write(config_str)
fout.close()

# Done.