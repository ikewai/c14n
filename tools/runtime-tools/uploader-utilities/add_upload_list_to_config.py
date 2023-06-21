import json, sys

# Load the config file specified as the first command line argument
fin = open(sys.argv[1], "rt")
fin_string = str(fin.read())
fin.close()
upload_config = json.loads(fin_string)

# Default permission setup for uploading data for public access.
dir_permissions = [
    {
        "permission": "READ",
        "recursive": True,
        "username": "public"
    }
]

# inject dir_permissions
for upload_dir in upload_config['upload']:
    upload_dir['dir_permissions'] = dir_permissions

# write updated config to disk
fout = open(sys.argv[2], "wt")
json.dump(upload_config, fout, indent=4)
fout.close()