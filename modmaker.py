import os

output_file = "module_info.json"
outbuf = open(output_file, "w")

for subdir, dirs, files in os.walk("./"):
    for directory in dirs:
        if not os.path.isdir(directory) or directory.startswith("."):
            continue
        print(directory)
        outbuf.write("{\n")
        outbuf.write("    \"display_name\": \"{charactername}\",\n".format(charactername = directory))
        outbuf.write("    \"path_in_folder\": \"{charactername}\",\n".format(charactername = directory))
        outbuf.write("    \"num_costumes\": 8,\n")
        outbuf.write("    \"aliases\": []\n".format(charactername = directory))
        outbuf.write("},\n")

outbuf.close()
