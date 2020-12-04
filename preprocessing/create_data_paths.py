# coding=utf-8
import json
import glob


def create_url_list(folder_path):
    result = {
        "path" : []
    }
    files = glob.glob(folder_path + '/*/')
    result["path"] = files
    return result


with open('preprocessing/data_paths.json', 'w', encoding="utf-8") as uni:
     json.dump(create_url_list("/mnt/f/KHTN/"), uni, ensure_ascii=False)