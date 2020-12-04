import sys
import re

def split_sentence(s, n):
    s = s.lower().replace('\xa0', ' ').replace('&', '').replace('\n',' ').replace('\t', ' ')
    s = match_special_syl(s)[0]
    s = re.sub(
        r'[^a-zAÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶEÉÈẺẼẸÊẾỀỂỄỆIÍÌỈĨỊOÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴĐaáàảãạâấầẩẫậăắằẳẵặeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵđA-Z\s]',
        ' ', s)
    tokens = [token for token in s.split(" ") if len(token) > 0]
    tokens = (n-1) * ["PAD"] + tokens + (n-1) * ["PAD"]
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
    return str, {"date" : date, "email" : email, "url" : url, "number" : number}

def match_date(str):
    date = re.findall(r"\d+\/\d+\/\d+|\d+\/\d+|\d+-\d+-\d+|\d+-\d+", str)
    return re.sub(r"\d+\/\d+\/\d+|\d+\/\d+|\d+-\d+-\d+|\d+-\d+", "DATE", str), date

def match_email(str):
    email = re.findall(r"(\.|[a-z]|[A-Z]|[0-9])*@(\.|[a-z]|[A-Z]|[0-9])*", str)
    return re.sub(r"(\.|[a-z]|[A-Z]|[0-9])*@(\.|[a-z]|[A-Z]|[0-9])*", "EMAIL", str), email

def match_url(str):
    url = re.findall(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})", str)
    return re.sub(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})", "URL", str), url

def match_number(str):
    number = re.findall(r"\d+", str)
    return re.sub(r"\d+", "NUMBER", str), number
