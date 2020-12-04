import sys
import time
import json

threshold = 20
filenames = ["unigram", "bigram", "trigram"]

for filename in filenames:
    print("----------" + filename + "---------------")
    with open('datasets/' + filename + '.txt', mode="r", encoding="utf-8") as fobj:
        dictionary = json.load(fobj)
        keys = [x for x in dictionary.keys()]
        count = 0
        for key in keys:
            count+=1
            if (count % 1000 == 0):
                print(count)
            if dictionary[key] <= threshold:
                del dictionary[key]
        print("Remove finished")
        with open('datasets/' + filename + '_' + str(threshold) + '.json', 'w', encoding='utf-8') as f:
            json.dump(dictionary, f, ensure_ascii=False)

print("Done!!!!!!")
