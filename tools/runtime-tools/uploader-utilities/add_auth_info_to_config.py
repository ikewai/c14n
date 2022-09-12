#!/bin/python3

import os, sys, json
# Currently a prototype, needs to be improved for robustness

if sys.argv[1] == None:
    print("No arg! Exiting")
    exit(1)
elif str(sys.argv[1]) == "":
    print("Arg Empty! Exiting")
    exit(1)

# Take arg 1 as the upload config file
config_file_name = str(sys.argv[1])
print(f"Adding auth variables to {config_file_name}!")
with open(config_file_name, "r") as config_file:
    upload_config: dict = json.loads(config_file.read())

# Inject auth variables from directly named environment variables.
# These are either set in the .env file during local-server testing or in
# default_environment when calling createActor().
upload_config['agave_options']['username'] = os.environ['IW_USERNAME']
upload_config['agave_options']['password'] = os.environ['IW_PASSWORD']
upload_config['agave_options']['api_key'] = os.environ['IW_API_KEY']
upload_config['agave_options']['api_secret'] = os.environ['IW_API_SECRET']


# then, write the changes to file
config_to_write = json.dumps(upload_config)

with open(config_file_name, "w") as config_file:
    config_file.write(config_to_write)