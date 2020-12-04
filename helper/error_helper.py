from python_extractor.helper.stringconstant import *
import re

f1 = open('helper/ngramdict/syllables.txt', 'r', encoding="utf-8")
f2 = open('helper/ngramdict/unigram_extractsign.txt', 'r', encoding="utf-8")
word_extractsign = {}
list_word = []
for sen in f2:
    part = sen.split(' ')
    if part[0] in word_extractsign:
        word_extractsign[part[0]] = max(word_extractsign[part[0]], int(part[1]))
    else:
        word_extractsign[part[0]] = int(part[1])

for sen in f1:
    list_word.append(sen.split())


def extractsign(word):
    tmp = ''
    textsign = ''
    kt = False
    for char in word:
        k = source.find(char)
        if k >= 0:
            t = vnCharacter.find(dest[k])
            if t >= 0:
                tmp = tmp + vnCharacterExtractsign[t]
            else:
                tmp = tmp + dest[k]
            textsign = sign[k]
            kt = True
        else:
            t = vnCharacter.find(char)
            if t >= 0:
                tmp = tmp + vnCharacterExtractsign[t]
            else:
                tmp = tmp + char
    if kt:
        tmp = tmp + textsign
    return tmp


def repairsign(word):
    index = -1
    if word in word_extractsign:
        index = word_extractsign[word]
    if index >= 0:
        return list_word[index][0]


def isforeign(word):
    list_foreign = ['w', 'f', 'j', 'z', 'ar', 'av', 'as', 'ag', 'br', 'ce', 'ci', 'ck', 'ec', 'er', 'ev', 'es', 'ea',
                    'et', 'el', 'ey',
                    'gl', 'ic', 'ir', 'is', 'iv', 'id', 'il', 'ka', 'nn', 'nd', 'nc', 'pp', 'pl', 'ov', 'yl', 'st',
                    'ub', 'ur', 'us', 'uv', 'ud', 'ion']
    for element in list_foreign:
        if str(element) in word:
            return word


def pre(word):
    if word[0] in upperCharacter:
        return word

    tmp = re.search(date, word)
    if tmp is not None:
        return tmp.string

    tmp = re.search(emailcheck, word)
    if tmp is not None:
        return tmp.string

    tmp = re.search(webcheck, word)
    if tmp is not None:
        return tmp.string

    tmp = re.search(numbercheck, word)
    if tmp is not None:
        return tmp.string


# print(extractsign("wyết"))
