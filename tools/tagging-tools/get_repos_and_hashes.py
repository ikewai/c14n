#!/bin/python3

import json, sys, subprocess, os

# All args are interpreted as libraries to clone.
manifest: dict = {}
output_filename = sys.argv[1]
repos = sys.argv[2::1]
for repo in repos: # args taken are implied to be URLs ending in .git
    subprocess.run(["/bin/bash", "-c", f"git clone {repo}"])


for repo_dir in os.listdir(): # assuming each directory under the current one is a repo
    hash = subprocess.run(["/bin/bash", "-c", f"cat {repo_dir}/.git/ORIG_HEAD"])

    # Go through each repo URL, and (naively) match the hashes to them, based on the directory names.
    for repo in repos:
        if repo.__contains__(repo_dir):
            # TODO check to ensure hash is valid
            manifest[repo] = hash

# Dump and write manifest to file.
manifest__str = json.dumps(manifest)
fname = output_filename
output_file = open(fname, "wt")
output_file.write(manifest__str)
output_file.close()