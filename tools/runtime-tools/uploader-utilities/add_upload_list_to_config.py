import json, sys

# load in the basic upload data
fin = open(sys.argv[1], "rt")
fin_string = str(fin.read())
fin.close()

upload_config = json.loads(fin_string)

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

fout = open(sys.argv[2], "wt")
json.dump(upload_config, fout, indent=4)
fout.close()


### the following seems weirdly organized, pending deletion
# load config file to place the new upload list into
#fin = open(sys.argv[2], "rt")
#fin_string = str(fin.read())
#fin.close()

#full_upload_config = json.loads(fin_string)

#full_upload_config['upload'] = upload_config['upload']

# write the new config
#fout = open(sys.argv[2], "wt")
#json.dump(full_upload_config, fout, indent=4)
#fout.close()