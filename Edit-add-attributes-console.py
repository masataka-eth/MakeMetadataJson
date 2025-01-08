import sys
import os
from datetime import datetime
import json
import random
import copy

# args = sys.argv
# print(args[1])

dict2 = {}
attlist = []
trait_type_list = ["わんぱく(Impish)","むじゃき(Naive)","てれや(Bashful)","がんばりや(Hardy)","すなお(Docile)"]

# make newFolder
new_dir_path = './' + datetime.now().strftime('%Y%m%d%H%M%S') + '_attributes-add'
os.mkdir(new_dir_path)

for num in range(1,150+1):  #1-10000
    # json → dict
    outputpath = "./attributes-add/" + str(num) + ".json"
    print(outputpath)
    json_open = open("./attributes-add/" + str(num) + ".json", "r", encoding="utf-8-sig")
    json_dict = json.load(json_open)

    attlist.clear()
    for idx in range(5):
        dict2["trait_type"] = trait_type_list[idx]
        dict2["value"] = random.randint(1,10)   # 1-10
        attlist.append(copy.deepcopy(dict2))
        dict2.clear
    json_dict["attributes"] += attlist

    print(json_dict)
    print(len(json_dict["attributes"]))

    # json file output
    outputpath = new_dir_path + '/' + str(num) + '.json'
    json_file = open(outputpath, mode='w',encoding='utf-8')
    json.dump(json_dict, json_file, indent=2, ensure_ascii=False)
    json_file.close()