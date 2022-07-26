#!/bin/python3

import json # For reading the JSON build requirements.
import sys # For reading execution arguments.
import subprocess # For executing the git clone.
import os # For listing directories.

# arg 1 is interpreted as the file to read from. 
# arg 2 is interpreted as the manifest file to create.
input_filename = sys.argv[1] # Intended format: [{"url": "https://github.com/ikewai/c14n.git", "branch": "main"}, {...}]
output_filename = sys.argv[2] # Intended format: {"https://github.com/ikewai/c14n": {"branch": "main", "hash": "..."}, {...}}

input_file = open(input_filename, "rt")
input_file__str = input_file.read()
repo_list = json.loads(input_file__str)

manifest: dict = {} # Intended format: {"https://github.com/ikewai/c14n": {"branch": "..." "hash": "..."}, {...}}

for repo in repo_list: # args taken are implied to be URLs ending in .git
    subprocess.run(["/bin/bash", "-c", f"git clone {repo['url']}"])
    manifest[repo]['branch'] = repo['branch']


for repo_dir in os.listdir(): # assuming each directory under the current one is a repo, TODO add validation

    # Go through each repo URL, and (naively) match the hashes to them, based on the directory names.
    for repo in repo_list:
        if repo["url"].__contains__(f"{repo_dir}.git"):
            repo_branch_filename = f"{repo_dir}/.git/refs/heads/{repo['branch']}"
            repo_branch_file = open(repo_branch_filename, "rt")
            hash = repo_branch_file.read()

            # Crude check to validate the hash. A git hash string is always 88 bytes.
            if hash.__sizeof__ is 88:
                manifest[repo]['hash'] = hash
            else:
                manifest[repo]['hash'] = "Error during hash acquisition."
            

# Dump and write manifest to file.
manifest__str = json.dumps(manifest)
output_file = open(output_filename, "wt")
output_file.write(manifest__str)
output_file.close()