# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, '../')
import numpy as np
from Python_extractor.Model.word_frequency import WordFrequency
from Python_extractor.helper.utils import *
from Python_extractor.helper.reader_helper import get_single_word_list, read_config_file
from Python_extractor.helper.error import total_error


config = read_config_file()


def check_is_constant(word):
    if "NUMBER" in word or "DATE" in word or "EMAIL" in word or "URL" in word:
        return True
    return False


def neighbors(index, words):
    result = ["", "", "", ""]
    if index > 0:
        result[1] = words[index - 1]
    if index > 1:
        result[0] = words[index - 2]
    if index < len(words) - 1:
        result[2] = words[index + 1]
    if index < len(words) - 2:
        result[3] = words[index + 2]
    return result


class Spell_check:
    __slots__ = ["_unigram", "_bigram", "_trigram", "_tokenizer", '_letters', '_single_words', '_stop_words',
                 '_correction_threshold', '_error_threshold']

    def __init__(self, tokenizer=None):
        print("Loading ...")
        self._correction_threshold = config['c_thres']
        self._error_threshold = config['e_thres']
        self._tokenizer = parse_into_words
        if tokenizer is not None:
            self._tokenizer = tokenizer
        self._unigram, self._bigram, self._trigram = (WordFrequency(), WordFrequency(), WordFrequency())
        self._unigram.load_dictionary("dataset/new_unigram_5.json")
        self._bigram.load_dictionary("dataset/new_bigram_5.json")
        self._trigram.load_dictionary("dataset/new_trigram_5.json")
        self._letters = ['a', 'ă', 'â', 'b', 'c', 'd', 'đ', 'e', 'ê', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'ô', 'ơ',
                         'p', 'q', 'r', 's', 't', 'j', 'w', 'f', 'u', 'ư', 'v', 'x', 'y', 'á', 'à', 'ả', 'ã', 'ạ', 'ấ',
                         'ầ', 'ẩ', 'ẫ', 'ậ', 'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ', 'é', 'è', 'ẻ', 'ẽ', 'ẹ', 'ế', 'ề', 'ể', 'ễ', 'ệ',
                         'í', 'ì', 'ỉ', 'ĩ', 'ị', 'ó', 'ò', 'ỏ', 'õ', 'ọ', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ớ', 'ờ', 'ở', 'ỡ',
                         'ợ', 'ú', 'ù', 'ủ', 'ũ', 'ụ', 'ứ', 'ừ', 'ử', 'ữ', 'ự', 'ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ']
        self._single_words = self.get_single_words()

    def spell_check(self, words):

        words = [formatSentence(word) for word in words]
        result = []
        response = []
        for i in range(len(words)):

            result.append(self.correct(words[i], neighbors(i, words)))

            if not result[i][0]:
                response.append({"wordPos": i, "alternativeWord": result[i][1]})

        print(response)
        print("----------------------------------------------------------------")
        return response

    def correct(self, word, neighbors, is_non_word=False):
        word = ENSURE_UNICODE(word)
        if check_is_constant(word) or len(word) <= 1:
            return True, []
        current_word_probability = self.word_probability(word, neighbors)
        if current_word_probability > self._correction_threshold:
            return True, []

        candidates = set(total_error(word))

        if not candidates:
            return True, []

        result = []
        for item in candidates:
            tmp = self.word_probability(item, neighbors)
            if tmp > current_word_probability + self._error_threshold:
                result.append((item, tmp))

        result = sorted(result, key=lambda tup: tup[1], reverse=True)

        if len(result) > 0:
            print("------------------------------------------")
            print(word)
            print(current_word_probability)
            print(result[:min(5, len(result))])
            print("------------------------------------------")
            result = [i for i, j in result[:min(5, len(result))]]
            return False, result

        if is_non_word:
            return False, result
        else:
            return True, result

    def word_probability(self, word, neighbors):
        phrases = [neighbors[0] + " " + neighbors[1] + " " + word, neighbors[1] + " " + word + " " + neighbors[2],
                   word + " " + neighbors[2] + " " + neighbors[3]]
        probs = []
        for phrase in phrases:
            phrase = phrase.strip()
            if len(self._tokenizer(phrase)) == 2:
                total_words = self._bigram.total_words
                phrase = ENSURE_UNICODE(phrase)
                probs.append((self._bigram[phrase] + 1) / total_words)
            elif len(self._tokenizer(phrase)) == 3:
                total_words = self._trigram.total_words
                phrase = ENSURE_UNICODE(phrase)
                probs.append((self._trigram[phrase] + 1) / total_words)
        return self.geo_mean_logarithm(probs)

    def check_word_exist(self, i, words):
        word = words[i]
        if not word in self._single_words:
            return False
        return True

    def split_words(self, text):
        text = ENSURE_UNICODE(text)
        return self._tokenizer(text)

    def real_word_detection(self, i, words):

        front_words = words[i]
        if i > 0:
            front_words = words[i - 1] + " " + front_words
            front_words = not (
                        front_words in self._bigram or check_is_constant(words[i - 1]))

        back_words = words[i]
        if i < len(words) - 1:
            back_words = back_words + " " + words[i + 1]
            back_words = not (
                        back_words in self._bigram or check_is_constant(words[i + 1]))

        if front_words and back_words:
            return False
        return True

    @staticmethod
    def geo_mean_logarithm(iterable):
        a = np.array(iterable)
        try:
            return np.log(a.prod() ** (1.0 / len(a)))
        except Exception as e:
            return 0

    def get_single_words(self, threshold=20):
        default_list = get_single_word_list()
        single_words = set(default_list)
        for word in self._unigram.dictionary:
            if self._unigram[word] > threshold:
                single_words.add(word)
        return single_words


spell = Spell_check()
spell.spell_check("Cả 8 gia đình ở huyện Can Lộc, Hà Tĩnh có đơn trình báo mất liên lajj với người thn trên đường đi Anh nhận được điện")
