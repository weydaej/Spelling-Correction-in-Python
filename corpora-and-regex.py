# Corpora and Regex
import nltk
import os
import sys
# nltk.download('brown')
from nltk.corpus import brown # Brown University Stanford Corpus of Present-Dat American English

# x = nltk.data.load('big.txt', format='raw')
# print(x[:500])
# importing in text format makes things 1000x better
x = nltk.data.load('big.txt', format='text')
# print(x[:500])
# and you can do things like this
# print("the" in x)
# print("student" in x)
# print("run" in x)
# print("acaudate" in x)
# print("jaculation" in x)

from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader('./', ['wordlist.txt', 'wordlist2.txt'])
print(reader.words())
print(reader.fileids())


# Lemmatization & Stemming
# nltk.download('wordnet')
# nltk.download('punkt')
from nltk.stem.porter import *
stemmer = PorterStemmer()
print(stemmer.stem('loving'))

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
print(wnl.lemmatize('monsters'))