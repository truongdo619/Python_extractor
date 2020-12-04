import gzip
import json
import sys
from collections import Counter
import os
import time

sys.path.insert(0, './')
from concurrent.futures import ProcessPoolExecutor
from helper.reader_helper import load_jsonl_from_gz
from preprocessing.formatting import split_sentence
from helper.multithread_helper import multithread_helper


def remove_by_threshold(d, thres = 5):
    return Counter({k: c for k, c in d.items() if c >= thres})


class Pre_processing(object):
    __slots__ = [
        "_unigram_dict",
        "_bigram_dict",
        "_trigram_dict",
        "_sentences_num",
        "_data_paths",
        "_batch_paths"
    ]

    def __init__(self):
        self._sentences_num = 0
        self._unigram_dict, self._bigram_dict, self._trigram_dict = Counter(), Counter(), Counter()
        self._data_paths = self.read_data_path()

    @staticmethod
    def read_data_path():
        with open('preprocessing/data_paths.json') as f:
            data = json.load(f)
        return data

    def generate_ngrams(self, sentence, n):
        ngrams = split_sentence(sentence, n)
        if n == 1:
            self._unigram_dict.update(Counter(ngrams))
        elif n == 2:
            self._bigram_dict.update(Counter(ngrams))
        else:
            self._trigram_dict.update(Counter(ngrams))

    def ngrams(self, id, path):
        sentences_num = 0
        with gzip.open(path + "remove.gz", 'rt') as f:
            sentences = f.readlines()
            total_sens = len(sentences)
            print(total_sens)
            for i, sentence in enumerate(sentences):

                if i % 1000 == 0:
                    print("Part " + str(id) + " : " + str(i) + "/" + str(total_sens))

                if len(sentence) > 10:
                    sentences_num += 1

                    ngrams = split_sentence(sentence, 1)
                    self._unigram_dict.update(Counter(ngrams))

                    ngrams = split_sentence(sentence, 2)
                    self._bigram_dict.update(Counter(ngrams))

                    ngrams = split_sentence(sentence, 3)
                    self._trigram_dict.update(Counter(ngrams))

        print("Part " + str(id) + " : " + str(sentences_num))



    @property
    def unigram_dict(self):
        return self._unigram_dict

    @property
    def bigram_dict(self):
        return self._bigram_dict

    @property
    def trigram_dict(self):
        return self._trigram_dict

    @property
    def batch_paths(self):
        return self._batch_paths

    @property
    def data_paths(self):
        return self._data_paths

    @unigram_dict.setter
    def unigram_dict(self, value):
        self._unigram_dict = value

    @bigram_dict.setter
    def bigram_dict(self, value):
        self._bigram_dict = value

    @trigram_dict.setter
    def trigram_dict(self, value):
        self._trigram_dict = value

    @property
    def sentences_num(self):
        return self._sentences_num


if __name__ == '__main__':
    ####Generate data_batch####
    # pre_processing = Pre_processing()
    # paths = pre_processing.data_paths["path"]
    # executor = ProcessPoolExecutor(max_workers=5)
    # for i in range(len(paths)):
    #     if not os.path.exists("dataset/categories/general/part_" + str(i)):
    #         os.makedirs("dataset/categories/general/part_" + str(i))
    #     executor.submit(pre_processing.ngrams, i, paths[i])


    ####Genertate n_gram dictionary####


    # pre_processing = Pre_processing()
    # data_paths = pre_processing.data_paths["path"]
    #
    # for id, path in enumerate(data_paths):
    #    print(id)
    #    pre_processing.ngrams(path)
    # multithread_helper(data_paths, pre_processing.ngrams)
    #
    # print(time.time() - start_time)
    # pre_processing.unigram_dict = remove_by_threshold(pre_processing.unigram_dict)
    # pre_processing.bigram_dict =  remove_by_threshold(pre_processing.bigram_dict)
    # pre_processing.trigram_dict = remove_by_threshold(pre_processing.trigram_dict)

    pre_processing = Pre_processing()
    data_paths = pre_processing.data_paths["path"]

    print(len(data_paths))
    for id, path in enumerate(data_paths):
       pre_processing.ngrams(id, path)

    pre_processing.unigram_dict = remove_by_threshold(pre_processing.unigram_dict)
    pre_processing.bigram_dict =  remove_by_threshold(pre_processing.bigram_dict)
    pre_processing.trigram_dict = remove_by_threshold(pre_processing.trigram_dict)

    with open('dataset/categories/KHTN/new/unigram.json', 'w', encoding="utf-8") as uni:
        json.dump(pre_processing.unigram_dict, uni, ensure_ascii=False)
    with open('dataset/categories/KHTN/new/bigram.json', 'w', encoding="utf-8") as bi:
        json.dump(pre_processing.bigram_dict, bi, ensure_ascii=False)
    with open('dataset/categories/KHTN/new/trigram.json', 'w', encoding="utf-8") as tri:
        json.dump(pre_processing.trigram_dict, tri, ensure_ascii=False)

