from Python_extractor.helper.error_helper import *
import string
import random


def typingerror(word, list_tmp):
    # Ấn thừa ký tự xem có nằm trong từ điển không
    word_extract = extractsign(word)

    tmp = repairsign(word_extract)
    if tmp is not None:
        list_tmp.append(tmp)

    for i in range(0, len(word_extract) + 1):
        for x in string.ascii_lowercase:
            tmp = word_extract
            tmp = tmp[0:i] + x + tmp[i:len(tmp)]
            tmp = repairsign(tmp)
            if tmp != None:
                list_tmp.append(tmp)

    # THeo 3 dòng của bàn phím
    for i in range(0, len(word_extract)):
        tmp = word_extract
        tmp = tmp[0:i] + tmp[i + 1:len(tmp)]
        tmp = repairsign(tmp)
        if tmp is not None:
            list_tmp.append(tmp)
        for j in range(0, len(keyboard)):
            index = keyboard[j].find(word_extract[i])
            if index - 1 >= 0:
                tmp = word_extract
                tmp = tmp[0:i] + keyboard[j][index - 1] + tmp[i:len(tmp)]
                tmp = repairsign(tmp)
                if tmp is not None:
                    list_tmp.append(tmp)

            if index + 1 < len(keyboard[j]):
                tmp = word_extract
                tmp = tmp[0:i] + keyboard[j][index + 1] + tmp[i:len(tmp)]
                tmp = repairsign(tmp)
                if tmp is not None:
                    list_tmp.append(tmp)


# Đổi âm vần ở cuối, dựa vào bộ đã có tự định nghĩa
def end(word, list_tmp):
    for i in range(0, endErrorLength):
        if len(word) > len(end_error[i]):
            if word[len(word) - len(end_error[i]):len(word)] == end_error[i]:
                for t in range(i - 4, i + 4):
                    if 0 <= t < endErrorLength and t != i:
                        if endErrorCheck[t] == endErrorCheck[i]:
                            tmp = word[0:len(word) - len(end_error[i])] + end_error[t]
                            list_tmp.append(tmp)


# Đổi ký tự đầu, dựa vào bộ tự định nghĩa
def start(word, list_tmp):
    for i in range(0, startErrorLength):
        if len(word) > len(startError[i]):
            if word[0:len(startError[i])] == startError[i]:
                for t in range(i - 4, i + 4):
                    if 0 <= t < startErrorLength and t != i:
                        if startErrorCheck[t] == startErrorCheck[i]:
                            tmp = startError[t] + word[len(startError[i]):len(word)]
                            list_tmp.append(tmp)


# Đổi dấu
def sign(word, list_tmp):
    word_exsign = extractsign(word)
    if signError.find(word_exsign[len(word_exsign) - 1]) >= 0 and signError.find(
            word_exsign[len(word_exsign) - 1]) < signErrorLength:
        for i in range(signErrorLength):
            tmp = word_exsign[0:len(word_exsign) - 1] + signError[i]
            tmp = repairsign(tmp)
            if tmp is not None:
                list_tmp.append(tmp)


def total_error(word):
    list_tmp = []
    typingerror(word, list_tmp)
    end(word, list_tmp)
    start(word, list_tmp)
    sign(word, list_tmp)
    return list_tmp