#!/bin/python3

# This script makes directories from a JSON-formatted list.
# Usage: python3 mkdir_from_json.py [file_to_read]

import sys # For reading the execution argument(s).
import json # For reading the JSON-formatted list.
import subprocess # For executing mkdir.

# Check for argument issues
if sys.argv[1] == None:
    print("No arg! Exiting.")
    exit(1)
elif not str(sys.argv[1]).__contains__(".json"):
    print("Arg needs to be a json-formatted list. Exiting.")
    exit(1)

# Take arg 1 as the json file to read
dirs_file_name = str(sys.argv[1])
print(f"Making directories from {dirs_file_name}!")

# Open and read the file
with open(dirs_file_name) as dirs_file:
    dirs: list = json.loads(dirs_file.read())
print(f"Dirs are: {dirs}!")

# Make each directory
for dir in dirs:
    subprocess.run(["/bin/bash", "-c", f"mkdir -p {dir}"])