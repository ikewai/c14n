#!/bin/python3

# This script generates a manifest of the repos and their associated current commit hashes
# that were involved in the production of the container, as defined in the arg 1 file.
# To do so, it pulls each repo, gets the hash, saves info from each, then deletes the repo.

import json # For reading the JSON build requirements.
import sys # For reading execution arguments.
import subprocess # For executing the git clone.
import os # For listing directories.
from datetime import datetime # For adding timestamps to the manifest.

# arg 1 is interpreted as the file to read from. 
# arg 2 is interpreted as the manifest file to create.
input_filename = sys.argv[1] # Intended format: [{"url": "https://github.com/ikewai/c14n.git", "branch": "main"}, {...}]
output_filename = sys.argv[2] # Intended format: {"https://github.com/ikewai/c14n": {"branch": "main", "hash": "..."}, {...}}

input_file = open(input_filename, "rt")
input_file__str = input_file.read()
repo_list = json.loads(input_file__str)

manifest: dict = {} # Intended format: {"https://github.com/ikewai/c14n": {"branch": "..." "hash": "..."}, {...}}

for repo in repo_list: # args taken are implied to be URLs ending in .git
    manifest[repo['url']] = {} # necessary to prevent keyerror
    # Add timestamp
    manifest[repo['url']]['timestamp'] = datetime.now().isoformat()
    # Clone repo
    subprocess.run(["/bin/bash", "-c", f"git clone {repo['url']}"])
    # Set branch name in manifest
    manifest[repo['url']]['branch'] = repo['branch']


for repo_dir in os.listdir():

    # Basic validation, assumes that the directory is a repo if it has a .git file inside.
    dir_contents = os.listdir(repo_dir)
    if ".git" not in dir_contents:
        continue

    # Go through each repo URL, and (naively) match the hashes to them, based on the directory names.
    for repo in repo_list:
        if repo['url'].__contains__(f"{repo_dir}.git"):
            repo_branch_filename = f"{repo_dir}/.git/refs/heads/{repo['branch']}"
            repo_branch_file = open(repo_branch_filename, "rt")
            hash = repo_branch_file.read().strip('\n')

            # Crude check to validate the hash. A git hash string is always 89 bytes in python.
            if hash.__sizeof__() == 89:
                manifest[repo['url']]['hash'] = hash
            else:
                manifest[repo['url']]['hash'] = "Error during hash acquisition."

    # Delete the repo after the data is extracted.
    subprocess.run(["/bin/bash", "-c", f"rm -r {repo_dir}"])



# Dump and write manifest to file.
manifest__str = json.dumps(manifest)
output_file = open(output_filename, "wt")
output_file.write(manifest__str)
output_file.close()