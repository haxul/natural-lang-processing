"""

Постройте биграммную языковую модель на основе корпуса:

<s> Вася любит мороженое </s>
<s> Лена любит малину </s>
<s> Вася любит Лену </s>
<s> Георгий ест мороженое </s>
<s> Лена рисует яблоко </s>
<s> Георгий любит Катю </s>
<s> Георгий любит смотреть, как Лена ест мороженое </s>

Упорядочите предложения по убыванию оценок вероятностей на основе построенной языковой модели.

"""

from collections import Counter

corpus = """<s> Вася любит мороженое </s>
<s> Лена любит малину </s>
<s> Вася любит Лену </s>
<s> Георгий ест мороженое </s>
<s> Лена рисует яблоко </s>
<s> Георгий любит Катю </s>
<s> Георгий любит смотреть, как Лена ест мороженое </s>
"""

arr = corpus.split()
words_count_map = Counter(arr)
bi_grams = {}

for i in range(1, len(arr)):
    if arr[i] in ("<s>", "</s>"):
        continue
    cur_bi_gram = (arr[i], arr[i - 1])
    if cur_bi_gram in bi_grams:
        bi_grams[cur_bi_gram] += 1
    else:
        bi_grams[cur_bi_gram] = 1


def compute_score(s: str) -> float:
    score = 1
    arr = s.split()
    for i in range(1, len(arr) - 1):
        cur_bi_gram = (arr[i], arr[i - 1])
        bi_gram_amount = bi_grams.get(cur_bi_gram)
        if not bi_gram_amount:
            return 0
        all_word_amount = words_count_map.get(cur_bi_gram[1])
        if not all_word_amount:
            return 0
        score *= bi_gram_amount / all_word_amount
    return score


print(compute_score("<s> Вася любит Катю </s>"))
print(compute_score("<s> Лена любит мороженое </s>"))
print(compute_score("<s> Лена рисует малину </s>"))
