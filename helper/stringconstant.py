symbolString = "\",\\.'\\*?/:;\\-_+=#$%&Z*!<>\\[{}\\]()&^•€“”…..."

titleList = ["A1", "GD&ĐT", "GDĐT", "GS", "GS.TS", "GS.TS.", "GS.TSKH", "GS.TSKH.", "HCM", "HN", "HĐND", "I", "II",
        "III", "IV", "IX", "Mr", "Mr.", "Mrs.", "Ms", "NV1", "NV2", "PGS", "PGS.TS", "PGS.TS.", "PGS.TSKH",
        "PGS.TSKH.", "TP.", "TP.HCM", "TS", "TS.", "ThS.", "Tp.", "U.N", "UBND", "V", "VI", "VII", "VIII", "X",
        "XHNV", "XI", "XII", "XIII", "XIV", "XIX", "XV", "XVI", "XVII", "XVIII", "XX", "XXI", "a.m", "gs.ts",
        "p.m", "pgs.ts", "tp.", "ĐH", "ĐHQG", "ĐHQGHN"]

endSentenceCharacter = ".!?;:…"

middleSymbol = "-/\\><[],"

upperCharacter = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬĐÈẺẼÉẸÊỀỂỄẾỆÌỈĨÍỊÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢÙỦŨÚỤƯỪỬỮỨỰỲỶỸÝỴ"

date = "(([0-9]{2}|[0-9])(-|/)([0-9]{2}|[0-9])(-|/)([0-9]{4}))(.*)"

emailcheck = "[a-zA-Z0-9\",\\.'\\*?/:;\\-_+=#$%&*!<>\\[{}\\]()&^•€“”…]+" + "@" + "[a-zA-Z0-9\",\\.'\\*?/:;\\-_+=#$%&Z*!<>\\[{}\\]()&^•€“”…]+[a-zA-Z]+(.*)"

webcheck = "(http://|https://|www.|//|ftp).*(.com|.vn|.org)?(.*)"

numbercheck = "[" + symbolString + "]*" + "\\-?\\d+\\.?(\\d+)?(k|g|MB|GB|Mb|,|...|%|h)?" + "[" + symbolString + "]*"

_length = 60

source = "àảãáạằẳẵắặầẩẫấậèẻẽéẹềểễếệìỉĩíịòỏõóọồổỗốộờởỡớợùủũúụừửữứựỳỷỹýỵ"

dest = "aaaaaăăăăăâââââeeeeeêêêêêiiiiioooooôôôôôơơơơơuuuuuưưưưưyyyyy"

sign = "frxsjfrxsjfrxsjfrxsjfrxsjfrxsjfrxsjfrxsjfrxsjfrxsjfrxsjfrxsj"

fullCharacter = "ABCDEGHIKLMNOPQRSTUVXYÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬĐÈẺẼÉẸÊỀỂỄẾỆÌỈĨÍỊÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢÙỦŨÚỤƯỪỬỮỨỰỲỶỸÝỴabcdeghiklmnopqrstuvxyàảãáạăằẳẵắặâầẩẫấậđèẻẽéẹêềểễếệìỉĩíịòỏõóọôồổỗốộơờởỡớợùủũúụưừửữứựỳỷỹýỵ"

vowel = "aăâeêioôơuưy"

vnCharacter = "ăâêôơưđ"

vnCharacterExtractsign = ["aw", "aa", "ee", "oo", "ow", "uw", "dd"]

keyboard = ["qwertyuiop[]", "asdfghjkl;'", "zxcvbnm,./"]

startErrorLength = 31

endErrorLength = 106

startError = ["ch", "tr", "d", "gi", "d", "gi", "nh", "d", "gi", "r",
        "d", "gi", "v", "hw", "ng", "qu", "w", "l", "n", "s", "x", "dì", "gì",
        "dĩ", "gĩ", "dỉ", "gỉ", "dị", "gị", "dí", "gí"]

startErrorCheck = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4,
        5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9,
        10, 10, 11, 11, 12, 12, 13, 13]

end_error = ["c", "t", "n", "ng", "ai", "ay", "ài", "ày", "ái", "áy", "ải", "ảy", "ãi", "ãy", "ại", "ạy",
        "em", "êm", "èm", "ềm", "ém", "ếm", "ẻm", "ểm", "ẽm", "ễm", "ẹm", "ệm",
        "êch", "êt", "ềch", "ềt", "ếch", "ết", "ểch", "ểt", "ễch", "ễt", "ệch", "ệt",
        "im", "iêm", "ìm", "iềm", "ím", "iếm", "ỉm", "iểm", "ĩm", "iễm", "ịm", "iệm",
        "iêu", "iu", "iều", "ìu", "iếu", "íu", "iểu", "ỉu", "iễu", "ĩu", "iệu", "ịu",
        "iêu", "ươu", "iều", "ườu", "iếu", "ướu", "iểu", "ưởu", "iễu", "ưỡu", "iệu", "ượu",
        "oai", "oi", "oài", "òi", "oái", "ói", "oải", "ỏi", "oãi", "õi", "oại", "ọi",
        "om", "ôm", "ơm", "òm", "ồm", "ờm", "óm", "ốm", "ớm", "ỏm", "ổm", "ởm", "õm", "ỗm", "ỡm", "ọm", "ộm", "ợm"]


endErrorCheck = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8,
        9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14,
        15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20,
        21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26,
        27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32,
        33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38,
        39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44,
        45, 45, 45, 46, 46, 46, 47, 47, 47, 48, 48, 48, 49, 49, 49, 50, 50, 50]

signErrorLength = 5

signError = "fsrxj"

