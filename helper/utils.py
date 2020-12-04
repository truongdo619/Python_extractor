import re
import sys
sys.path.insert(0, './')
import re
parenthesis_regex = re.compile('\(.+?\)')

import sys
sys.path.insert(0, './')
import json

##################### CONVERT TO TELEX ###############################

with open('dataset/telex.txt', encoding="utf-8") as f:
    data = json.load(f)

dau = ['á', 'à', 'ả', 'ã', 'ạ', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ', 'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ', 'é', 'è', 'ẻ', 'ẽ', 'ẹ', 'ế', 'ề',
       'ể', 'ễ', 'ệ', 'í', 'ì', 'ỉ', 'ĩ', 'ị', 'ó', 'ò', 'ỏ', 'õ', 'ọ', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ớ', 'ờ', 'ở', 'ỡ',
       'ợ', 'ú', 'ù', 'ủ', 'ũ', 'ụ', 'ứ', 'ừ', 'ử', 'ữ', 'ự', 'ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ']
telex_words = ['ă', 'â', 'ê', 'ô', 'ơ', 'ư', 'á', 'à', 'ả', 'ã', 'ạ', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ', 'ắ', 'ằ', 'ẳ', 'ẵ',
               'ặ', 'é', 'è', 'ẻ', 'ẽ', 'ẹ', 'ế', 'ề', 'ể', 'ễ', 'ệ', 'í', 'ì', 'ỉ', 'ĩ', 'ị', 'ó', 'ò', 'ỏ', 'õ',
               'ọ', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ớ', 'ờ', 'ở', 'ỡ', 'ợ', 'ú', 'ù', 'ủ', 'ũ', 'ụ', 'ứ', 'ừ', 'ử', 'ữ',
               'ự', 'ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ']
vowels = ['a', 'ă', 'â', 'ê', 'e', 'i', 'o', 'ô', 'ơ', 'y', 'u', 'ư', 'á', 'à', 'ả', 'ã', 'ạ', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ',
          'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ', 'é', 'è', 'ẻ', 'ẽ', 'ẹ', 'ế', 'ề', 'ể', 'ễ', 'ệ', 'í', 'ì', 'ỉ', 'ĩ', 'ị', 'ó',
          'ò', 'ỏ', 'õ', 'ọ', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ớ', 'ờ', 'ở', 'ỡ', 'ợ', 'ú', 'ù', 'ủ', 'ũ', 'ụ', 'ứ', 'ừ',
          'ử', 'ữ', 'ự', 'ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ']

def get_single_word_list():
    list = []
    try:
        with open('dataset/vi-dontu.dic', encoding="utf-8") as f:
            f.readline()
            for line in f:
                str = line.replace('\n', '').lower()
                list.append(str)
            f.close()
        return list
    except:
        pass
sac = [dau[index] for index in range(len(dau)) if index % 5 == 0]
huyen = [dau[index] for index in range(len(dau)) if index % 5 == 1]
hoi = [dau[index] for index in range(len(dau)) if index % 5 == 2]
nga = [dau[index] for index in range(len(dau)) if index % 5 == 3]
nang = [dau[index] for index in range(len(dau)) if index % 5 == 4]
khong_dau = ['a', 'â', 'ă', 'e', 'ê', 'i', 'o', 'ô', 'ơ',  'u', 'ư', 'y',]
telex = {
    'â' : 'aa',
    'ă' : 'aw',
    'ê' : 'ee',
    'ô' : 'oo',
    'ơ' : 'ow',
    'ư' : 'uw'
}
c_dau = ['s', 'f', 'x', 'j', 'r']
te_list = ['aa', 'aw', 'ee', 'oo', 'ow', 'uw']
def check_diacritic(str):
    result = sum([c in set(telex_words) for c in str])
    return result >= 1

def start_vowel(str):
    for index in range(len(str)):
        if str[index] in set(vowels):
            return index
    return 0

def remove_diacritic(str):
    for i in range(len(str)):
        if str[i] in sac:
            return (str.replace(str[i], khong_dau[sac.index(str[i])]), 's')
        if str[i] in huyen:
            return (str.replace(str[i], khong_dau[huyen.index(str[i])]), 'f')
        if str[i] in nga:
            return (str.replace(str[i], khong_dau[nga.index(str[i])]), 'x')
        if str[i] in hoi:
            return (str.replace(str[i], khong_dau[hoi.index(str[i])]), 'r')
        if str[i] in nang:
            return (str.replace(str[i], khong_dau[nang.index(str[i])]), 'j')
    return (str, '')

def convert_to_telex(str):
    return str.translate(str.maketrans(telex))

def convert(str, dau):
    result = []
    result.append(str + dau)
    if (len(str) > 1):
        if not (str[0] + str[1]) in te_list:
            result.append(str[0] + dau + str[1:])
    for i in range(1, len(str)-1):
        if (str[i-1] + str[i]) in te_list:
            result.append(str.replace(str[i-1] + str[i], str[i-1] + str[i] + dau))
        elif not (str[i] + str[i+1]) in te_list:
            result.append(str.replace(str[i], str[i] + dau))
    return set(result)

def convert_telex_to_word(str):
    na = str[:start_vowel(str)]
    pa = str[start_vowel(str):]
    na = na.replace("dd", "đ")
    if pa in data:
        pa = data[pa]
    return na + pa

##################### FORMATTING ###############################

def formatSentence(str):
    str = str.lower()
    #str = parenthesis_regex.sub('', str)
    tmp = match_special_syl(str)
    str = tmp[0]
    return re.sub(
        r'[^a-zAÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶEÉÈẺẼẸÊẾỀỂỄỆIÍÌỈĨỊOÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴĐaáàảãạâấầẩẫậăắằẳẵặeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵđA-Z\s]',
        ' ', str).strip()

def split_sentence(s, n):
    s = s.lower().replace('\xa0', ' ').replace('\n', ' ').replace('&', '')
    #s = parenthesis_regex.sub('', s)
    s = match_special_syl(s)[0]
    s = re.sub(
        r'[^a-zAÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶEÉÈẺẼẸÊẾỀỂỄỆIÍÌỈĨỊOÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴĐaáàảãạâấầẩẫậăắằẳẵặeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵđA-Z\s]',
        ' ', s)
    tokens = [token for token in s.split(" ") if len(token) > 1]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    ngrams = [" ".join(ngram) for ngram in ngrams]
    return ngrams


def get_word_pos(s):
    r = re.compile("[a-zAÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶEÉÈẺẼẸÊẾỀỂỄỆIÍÌỈĨỊOÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴĐaáàảãạâấầẩẫậăắằẳẵặeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵđA-Z]+")
    return [[m.start(), m.end()] for m in r.finditer(s)]

def get_all_words(s, n):
    s = s.lower().replace('\xa0', '')
    s = re.sub(
        r'[^a-zAÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶEÉÈẺẼẸÊẾỀỂỄỆIÍÌỈĨỊOÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴĐaáàảãạâấầẩẫậăắằẳẵặeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵđA-Z\s]',
        ' ', s)
    tokens = [token for token in s.split(" ") if len(token) > 0]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    ngrams = [" ".join(ngram) for ngram in ngrams]
    return ngrams

def match_special_syl(str):
    tmp = match_date(str)
    str = tmp[0]
    date = tmp[1]
    tmp = match_email(str)
    str = tmp[0]
    email = tmp[1]
    tmp = match_url(str)
    str = tmp[0]
    url = tmp[1]
    tmp = match_number(str)
    str = tmp[0]
    number = tmp[1]
    return ( str, { "date" : date, "email" : email, "url" : url, "number" : number})

def match_date(str):
    date = re.findall(r"\d+\/\d+\/\d+|\d+\/\d+|\d+-\d+-\d+|\d+-\d+", str)
    return (re.sub(r"\d+\/\d+\/\d+|\d+\/\d+|\d+-\d+-\d+|\d+-\d+", "DATE", str), date)

def match_email(str):
    email = re.findall(r"(\.|[a-z]|[A-Z]|[0-9])*@(\.|[a-z]|[A-Z]|[0-9])*", str)
    return (re.sub(r"(\.|[a-z]|[A-Z]|[0-9])*@(\.|[a-z]|[A-Z]|[0-9])*", "EMAIL", str), email)

def match_url(str):
    url = re.findall(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})", str)
    return (re.sub(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})", "URL", str), url)


##################### COMMON ###############################

def match_number(str):
    number = re.findall(r"\d+", str)
    return (re.sub(r"\d+", "NUMBER", str), number)

def ENSURE_UNICODE(s, encoding='utf-8'):
    if isinstance(s, bytes):
        return s.decode(encoding)
    return s

def load_file(filename, encoding):
    with open(filename, mode="r", encoding=encoding) as fobj:
        yield fobj.read()

def parse_into_words(str):
    return re.findall(r"\w+", str)


def generate_space(num):
    result = ''
    for i in range(num):
        result += ' '
    return result

def remove_html_tag(text):
    text = text.replace('\xa0', ' ').replace('\n', ' ').replace('&', '')
    regex = r'<[^>]*>'
    r = re.compile(regex)
    operation_list = [[m.start(), m.end()] for m in r.finditer(text)]
    start = 0
    result = ''
    operation_list.append([len(text), len(text)])
    for op in operation_list:
        end = op[0]
        result += text[start:end] + generate_space(op[1] - op[0])
        start = op[1]
        if (end == len(text)):
            break
    return result

def get_correct_pos(pos, content, special_characters):
    total = 0
    a = content.count("DATE")
    b = content.count("EMAIL")
    c = content.count("URL")
    d = content.count("NUMBER")
    if a != 0:
        total += special_characters['date'][a-1]
    if b != 0:
        total += special_characters['email'][b-1]
    if c != 0:
        total += special_characters['url'][c-1]
    if d != 0:
        total += special_characters['number'][d-1]
    return pos + total - a * 4 - b * 5 - c * 3 - d * 6

def pos_special_chars(special_chars):
    result = {}
    for key in special_chars.keys():
        count = 0
        tmp = []
        for item in special_chars[key]:
            count += len(item)
            tmp.append(count)
        result[key] = tmp
    return result

def editDistDP(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Min. operations = j
            elif j == 0:
                dp[i][j] = i  # Min. operations = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]