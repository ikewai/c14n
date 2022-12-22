#!/bin/python3
# A script to push every container in a list, in one pass.

import sys # For accessing execution args.
import subprocess # For spinning off docker pushes.
import json # For parsing the push list.

fin = sys.argv[1]
fin = open(fin, "rt")
container_list = json.loads(fin.read())

for c in container_list:
    cmd = f"docker push {c['image_name']}:{c['tag']}"
    subprocess.run(["/bin/bash", "-c", cmd])
    
    if c['tag'] == "latest":
        repo_hash = subprocess.run(["/bin/bash", "-c", "tools/tagging-tools/get_hash.sh"], capture_output=True).stdout.decode().strip("\n")
        cmd = f"docker push {c['image_name']}:{repo_hash}"
        subprocess.run(["/bin/bash", "-c", cmd])