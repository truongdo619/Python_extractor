import json

TCVN3=['µ', '¸', '¶', '·', '¹',
    '¨', '»', '¾', '¼', '½', 'Æ',
    '©', 'Ç', 'Ê', 'È', 'É', 'Ë',
    '®', 'Ì', 'Ð', 'Î', 'Ï', 'Ñ',
    'ª', 'Ò', 'Õ', 'Ó', 'Ô', 'Ö',
    '×', 'Ý', 'Ø', 'Ü', 'Þ',
    'ß', 'ã', 'á', 'â', 'ä',
    '«', 'å', 'è', 'æ', 'ç', 'é',
    '¬', 'ê', 'í', 'ë', 'ì', 'î',
    'ï', 'ó', 'ñ', 'ò', 'ô',
    '­', 'õ', 'ø', 'ö', '÷', 'ù',
    'ú', 'ý', 'û', 'ü', 'þ',
    '¡', '¢', '§', '£', '¤', '¥', '¦']

unicode=['à', 'á', 'ả', 'ã', 'ạ',
    'ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ',
    'â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ',
    'đ', 'è', 'é', 'ẻ', 'ẽ', 'ẹ',
    'ê', 'ề', 'ế', 'ể', 'ễ', 'ệ',
    'ì', 'í', 'ỉ', 'ĩ', 'ị',
    'ò', 'ó', 'ỏ', 'õ', 'ọ',
    'ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ',
    'ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ',
    'ù', 'ú', 'ủ', 'ũ', 'ụ',
    'ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự',
    'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ',
    'Ă', 'Â', 'Đ', 'Ê', 'Ô', 'Ơ', 'Ư']

UNICODE = "àảãáạằẳẵắặầẩẫấậèẻẽéẹềểễếệìỉĩíịòỏõóọồổỗốộờởỡớợùủũúụừửữứựỳỷỹýỵ";
CHARACTER_BELOW = "\u0061\u0103\u00E2\u0065\u00EA\u0069\u006F\u00F4\u01A1\u0075\u01B0\u0079";
HOOK_ABOVE = "\u0300\u0309\u0303\u0301\u0323";

TCVN3="".join(TCVN3)
unicode="".join(unicode)

def convert_tcvn3_to_unicode(text):
    return text.translate(str.maketrans(TCVN3, unicode))

def is_tcvn3_encoding(text):
    return '®' in text or '¶' in text or '¬' in text or '©' in text

def unicode_converter(input):
    result = input[0]
    for index in range(1, len(input)):
        hookIndex = HOOK_ABOVE.find(input[index])
        if hookIndex >= 0:
            charIndex = CHARACTER_BELOW.find(input[index-1])
            if charIndex >= 0:
                result = result[:-1]
                result += (UNICODE[charIndex * len(HOOK_ABOVE) + hookIndex])
                continue
        result += input[index]
    return result