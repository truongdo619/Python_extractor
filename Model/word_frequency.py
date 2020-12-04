from collections import Counter
import sys
sys.path.insert(0, './')
from Python_extractor.helper.utils import ENSURE_UNICODE, load_file
import json


class WordFrequency(object):
    __slots__ = [
        "_dictionary",
        "_total_words",
        "_unique_words"
    ]

    def __init__(self):
        self._dictionary = Counter()
        self._total_words = 0
        self._unique_words = 0

    def __contains__(self, key):
        key = ENSURE_UNICODE(key)
        key = key.lower()
        return key in self._dictionary

    def __getitem__(self, key):
        key = ENSURE_UNICODE(key)
        key = key.lower()
        return self._dictionary[key]

    def pop(self, key, default=None):
        key = ENSURE_UNICODE(key)
        key = key.lower()
        return self._dictionary.pop(key, default)

    @property
    def dictionary(self):
        return self._dictionary

    @property
    def total_words(self):
        return self._total_words

    @property
    def unique_words(self):
        return self._unique_words

    def keys(self):
        for key in self._dictionary.keys():
            yield key

    def items(self):
        for key in self._dictionary.keys():
            yield key, self._dictionary[key]

    def load_dictionary(self, filename, encoding="utf-8"):
        with open(filename, mode="r", encoding=encoding) as fobj:
            self._dictionary.update(json.load(fobj))
            self._update_dictionary()
            self.remove_by_threshold()

    def load_words(self, words):
        words = [ENSURE_UNICODE(w) for w in words]
        self._dictionary.update(
            [word.lower() for word in words]
        )
        self._update_dictionary()

    def add(self, word):
        word = ENSURE_UNICODE(word)
        self.load_words([word])

    def remove_words(self, words):
        words = [ENSURE_UNICODE(w) for w in words]
        for word in words:
            self._dictionary.pop(word.lower())
        self._update_dictionary()

    def remove(self, word):
        word = ENSURE_UNICODE(word)
        self._dictionary.pop(word.lower())
        self._update_dictionary()

    def remove_by_threshold(self, threshold=0):
        keys = [x for x in self._dictionary.keys()]
        for key in keys:
            if self._dictionary[key] <= threshold:
                self._dictionary.pop(key)
        self._update_dictionary()

    def _update_dictionary(self):
        self._total_words = sum(self._dictionary.values())
        self._unique_words = len(self._dictionary.keys())

# if __name__ == '__main__':
#     word = WordFrequency()
#     word.load_dictionary("dataset/bigram.txt")
#     print("Printed immediately.")
#     time.sleep(5)
#     print("Printed after 2.4 seconds.")

