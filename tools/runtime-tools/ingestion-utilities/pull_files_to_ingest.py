# Downloads files according to the "file_pulls" field in an ingestion config.

import json
import sys
import subprocess

fname = str(sys.argv[1])

with open(fname, "rt") as config_file:
    config_dict: dict = json.loads(config_file.read())

file_pulls: list(str) = config_dict["data"][0]["file_pulls"]

for pull in file_pulls:
    mkdir_command: str = f"mkdir -p {pull['placement_dir']}"
    subprocess.run("/bin/bash", "-c", mkdir_command)
    wget_command: str = f"wget {pull['url']} -O {pull['placement_dir']}/{pull['rename']}"
    subprocess.run(["/bin/bash", "-c", wget_command])