import sys
import os
from datetime import datetime
import json
import random
import copy

# args = sys.argv
# print(args[1])

# make newFolder
new_dir_path = './' + datetime.now().strftime('%Y%m%d%H%M%S') + '_image-update'
os.mkdir(new_dir_path)

for num in range(1,100+1):  #1-10000
    # json → dict
    outputpath = "./image-update/" + str(num) + ".json"
    print(outputpath)
    json_open = open("./image-update/" + str(num) + ".json", "r", encoding="utf-8-sig")
    json_dict = json.load(json_open)

    json_dict["image"] = "https://nft.aopanda.ainy-llc.com/app_lock/images/" + str(num) + ".gif"
    

    # json file output
    outputpath = new_dir_path + '/' + str(num) + '.json'
    json_file = open(outputpath, mode='w',encoding='utf-8')
    json.dump(json_dict, json_file, indent=2, ensure_ascii=False)
    json_file.close()