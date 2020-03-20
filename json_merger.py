import json
import glob

read_files = glob.glob("*.json")
output_list = []

for f in read_files:
    with open(f, "r") as infile:
        output_list.append(json.load(infile))
        print(f)

with open("merged_file.json", "w", encoding="utf8") as outfile:
    json.dump(output_list, outfile)
