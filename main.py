# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, '../')
from glob import glob
import os
import json, re

import enchant
from python_extractor.Model.spell_check import Spell_check


def remove_punctuation(s):
    return re.sub(
        r'[^a-zAÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶEÉÈẺẼẸÊẾỀỂỄỆIÍÌỈĨỊOÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴĐaáàảãạâấầẩẫậăắằẳẵặeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵđA-Z\s]',
        ' ', s)


def get_data_path(path):
    result = []
    for item in glob(path + "/*/"):
        if os.path.isfile(item + "sentences.json"):
            result.append(item)
    return result


class Extractor:
    def __init__(self):
        self.d = enchant.Dict("en_US")
        self.unique_sentences = set()
        self.spell_check = Spell_check()
        self.data_text = ""

    def check_sentence_length(self, item):
        return 255 >= len(item["content"]) > 20


    def read_json_file(self, path):
        data_text = ""
        # data_json = []
        unique_sentences = set()
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                if self.check_sentence_length(item):
                    # data_json.append(item)
                    if item["content"] not in unique_sentences:
                        data_text += item["content"] + "\n"
                        unique_sentences.add(item["content"])

        # with open('data.json', 'w', encoding="utf-8") as outfile:
        #     json.dump(data_json, outfile, ensure_ascii=False)
        #     outfile.close()

        with open("extracted_data/2020_12_01/sentence_err_plain_text.txt", "w", encoding="utf-8") as outfile:
            outfile.write(data_text)
            outfile.close()

    def check_sentences(self, base_folder, path):
        with open(path + "/sentences.json", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                wordlist = item["content"].split(" ")
                if self.check_sentence_length(item) and item["content"] not in self.unique_sentences and (not self.spell_check.spell_check(wordlist)):
                    self.data_text += item["content"] + "\n"
                    self.unique_sentences.add(item["content"])

        with open("extracted_data/" + base_folder + "/mrT_sentence_error.txt", "w", encoding="utf-8") as outfile:
            outfile.write(self.data_text)
            outfile.close()

    def run(self):
        # read_json_file("extracted_data/2020_12_01/sentence_err.json")
        base_folder = "2020_11_30"
        data_paths = get_data_path("../data/" + base_folder)[:1]
        print(data_paths)
        for path in data_paths:
            self.check_sentences(base_folder, path)


if __name__ == '__main__':
    extractor = Extractor()
    extractor.run()
