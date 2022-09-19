#!/bin/python3

# Arg 1: Key of environment variable where the list (json-style) of URLs is.
# Arg 2: Directory to place files into.

import os # For getting environment variables
import sys # For reading execution arguments
import json # For interpreting the list
import subprocess # For executing wgets

file_url_list_raw: str = os.environ[sys.argv[1]]
file_url_list: list(str) = json.loads(file_url_list_raw)

subprocess.run(["/bin/bash", "-c", f"mkdir -P {sys.argv[2]}"]) # Ensure that the output path exists.

for url in file_url_list:
    subprocess.run(["/bin/bash", "-c", f"wget {url} -P {sys.argv[2]}"])