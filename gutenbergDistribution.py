from nltk.corpus import gutenberg
import nltk
from collections import Counter
from matplotlib import pyplot as plt


hamlet = nltk.Text(gutenberg.words(fileids='shakespeare-hamlet.txt '))

#1
hamlet.concordance('Hamlet')

#2
print(hamlet.count('Hamlet'))

#3
hamlet.similar('Hamlet')

#4
hamlet.common_contexts('Hamlet', 'Horatio')
hamlet.dispersion_plot(["Hamlet",  "Horatio", "Ghost", "Polonius"])

#5
fdict = nltk.FreqDist(hamlet)
print('the number of uniqe tokens: ', len(fdict))
print(list(fdict.items())[:15])

#6
fdict.plot(50, cumulative=False)
fdict.plot(50, cumulative=True)

#7
print(fdict.hapaxes())

#8
words7 = [w for w in set(hamlet) if len(w) > 7 and fdict[w] > 7]
print('(1)список слов длиной больше 7 символов, частота появления в корпусе которых больше семи', words7)
words3 = [w for w in set(hamlet) if len(w) < 3 and fdict[w] < 3]
print('(2)список слов длинной меньше 3 символов, встречающихся в тексте меньше трех раз. ', words3)

#9
lexicon = len(hamlet)/len(fdict)
print('лексическое богатство текста = ', lexicon)

#10
def probability (word,word_num):
    prob = hamlet.count(word)/word_num
    return print('вероятность появления слова в корпусе = ', prob)

word = input('Введите слово: ')
word_num = input('Введите количество  слов в корпусе: ')
probability(word, int(word_num))

#11
print(hamlet.collocations())

#12
words12 = [w for w in set(hamlet) if len(w) > 12]
print('список слов текста, имеющих длину больше 12 символов: ', words12)

#13,14,15,16,17,18
word_lengths = [len(w) for w in hamlet]
print('распределение длин слов в тексте: ', word_lengths)
count = Counter(word_lengths)
print('максимальная длинна слова: ', max(word_lengths))
print('сколько раз встречается каждая длина слова:', count.most_common()[:14])
print('наиболее често встречаемая длина слова:', count.most_common()[:3])
plt.hist(word_lengths)
plt.show()