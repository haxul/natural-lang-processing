import pymorphy2
import re

file = open("/home/haxul/Development/workspaces/python/nlp/morph_analayzer/dataset_37845_1.txt", "r")
text = []
for w in file:
    words = re.split(r'\s+', w)
    for word in words:
        if not word:
            continue
        if word[len(word) - 1] == "," or word[len(word) - 1] == "." or word[len(word) - 1] == "!" or word[
            len(word) - 1] == '?':
            rw = word[:-1]
            text.append(rw)
        else:
            text.append(word)
file.close()

morph = pymorphy2.MorphAnalyzer()

result = []
for t in text:
    mp = morph.parse(t)[0]
    s = "%s{%s=%s}" % (t.capitalize(), mp.normal_form, mp.tag.POS)
    result.append(s)

f = open("/home/haxul/Development/workspaces/python/nlp/morph_analayzer/result.txt", "a")
count = -1
line = ""
for w in result:
    if count >= 3:
        f.write(f"{line}\n")
        count = -1
    count += 1
    line += w

f.close()
