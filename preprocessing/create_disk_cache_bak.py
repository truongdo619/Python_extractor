from diskcache import Index
from collections import Counter
import os
import json
import time

def remove_by_threshold_dict(d, thres = 3):
    return Counter({k: c for k, c in d.items() if c >= thres})

def remove_by_threshold(d, thres = 5):
    for k, c in d.items():
        if c < thres:
            del d[k]


class DiskCache(object):
    __slots__ = [
        "_unigram_disk_cache",
        "_bigram_disk_cache",
        "_trigram_disk_cache",
        "_dict_paths",
        "_unigram_dict",
        "_bigram_dict",
        "_trigram_dict"
    ]

    def __init__(self):
        # self._unigram_disk_cache = Index("/mnt/f/doit_spell_check_data/disk_cache/general/unigram")
        # self._bigram_disk_cache = Index("/mnt/f/doit_spell_check_data/disk_cache/general/bigram")
        # self._trigram_disk_cache = Index("/mnt/f/doit_spell_check_data/disk_cache/general/trigram")
        self._unigram_dict, self._bigram_dict, self._trigram_dict = Counter(), Counter(), Counter()
        self._dict_paths = self.read_dict_path()

    @staticmethod
    def read_dict_path():
        return [x[0] for x in os.walk("dataset/categories/general")]

    def merge_dict(self, id, path):
        start_time = time.time()

        unigram_dict_part, bigram_dict_part, trigram_dict_part = Counter(), Counter(), Counter()
        print("Part ", id, " : Loading")
        
        with open(path + "/unigram.json", mode="r", encoding="utf-8") as fobj:
            unigram_dict_part.update(json.load(fobj))
        #print("Unigram")
        #print(len(unigram_dict_part))
        #unigram_dict_part = remove_by_threshold(unigram_dict_part)
        print(len(unigram_dict_part))

        with open(path + "/bigram.json", mode="r", encoding="utf-8") as fobj:
            bigram_dict_part.update(json.load(fobj))
        #print("Bigram")
        #print(len(bigram_dict_part))
        #bigram_dict_part = remove_by_threshold(bigram_dict_part)
        print(len(bigram_dict_part))

        with open(path + "/trigram.json", mode="r", encoding="utf-8") as fobj:
            trigram_dict_part.update(json.load(fobj))
        #print("Trigram")
        #print(len(trigram_dict_part))
        #trigram_dict_part = remove_by_threshold(trigram_dict_part)
        print(len(trigram_dict_part))

        self._unigram_dict.update(unigram_dict_part)
        self._bigram_dict.update(bigram_dict_part)
        self._trigram_dict.update(trigram_dict_part)
        print("------------------------------------------------")
        print(len(self._unigram_dict))
        print(len(self._bigram_dict))
        print(len(self._trigram_dict))
        print("------------------------------------------------")

        if (id + 1) % 50 != 0 and id < 222:
            return


        self._unigram_dict = remove_by_threshold_dict(self._unigram_dict)
        self._bigram_dict = remove_by_threshold_dict(self._bigram_dict)
        self._trigram_dict = remove_by_threshold_dict(self._trigram_dict)

        with open('dataset/categories/big_part_' + str(int((id + 1) / 50)) + '/unigram.json', 'w', encoding="utf-8") as uni:
            json.dump(self._unigram_dict, uni, ensure_ascii=False)
        with open('dataset/categories/big_part_' + str(int((id + 1) / 50)) + '/bigram.json', 'w', encoding="utf-8") as bi:
            json.dump(self._bigram_dict, bi, ensure_ascii=False)
        with open('dataset/categories/big_part_' + str(int((id + 1) / 50)) + '/trigram.json', 'w', encoding="utf-8") as tri:
            json.dump(self._trigram_dict, tri, ensure_ascii=False)

        # count = 0
        # for key in self._unigram_dict.keys():
        #     count+= 1
        #     if count % 10000 == 0:
        #         print(count)
        #     try:
        #         self._unigram_disk_cache[key] += self._unigram_dict[key]
        #     except:
        #         self._unigram_disk_cache[key] = self._unigram_dict[key]
        # print("Part ", id, " : Unigram done!!!")
        #
        # count = 0
        # for key in self._bigram_dict.keys():
        #     count+= 1
        #     if count % 10000 == 0:
        #         print(count)
        #
        #     try:
        #         self._bigram_disk_cache[key] += self._bigram_dict[key]
        #     except:
        #         self._bigram_disk_cache[key] = self._bigram_dict[key]
        # print("Part ", id, " : Bigram done!!!")
        #
        # count = 0
        # for key in self._trigram_dict.keys():
        #     count+= 1
        #     if count % 10000 == 0:
        #         print(count)
        #     try:
        #         self._trigram_disk_cache[key] += self._trigram_dict[key]
        #     except:
        #         self._trigram_disk_cache[key] = self._trigram_dict[key]
        # print("Part ", id, " : Trigram done!!!")
        #
        # print("Part ", id, " : Loading done!!!")

        print(time.time() - start_time )

        self._unigram_dict, self._bigram_dict, self._trigram_dict = Counter(), Counter(), Counter()

        return

    @property
    def dict_paths(self):
        return self._dict_paths


if __name__ == '__main__':

    disk_cache = DiskCache()
    paths = disk_cache.dict_paths
    paths.pop(0)

    for id, path in enumerate(paths):
        disk_cache.merge_dict(id, path)

    # remove_by_threshold(self._unigram_disk_cache)
    # remove_by_threshold(self._bigram_disk_cache)
    # remove_by_threshold(self._trigram_disk_cache)

    # self._unigram_disk_cache.close()
    #
    # self._bigram_disk_cache.close()
    #
    # self._trigram_disk_cache.close()
