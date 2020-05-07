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

# from nltk.corpus.reader import WordListCorpusReader
# reader = WordListCorpusReader('./', ['wordlist.txt', 'wordlist2.txt'])
# print(reader.words())
# print(reader.fileids())


### Lemmatization & Stemming
# nltk.download('wordnet')
# nltk.download('punkt')

# from nltk.stem.porter import *
# stemmer = PorterStemmer()
# print(stemmer.stem('loving'))

# from nltk.stem import WordNetLemmatizer
# wnl = WordNetLemmatizer()
# print(wnl.lemmatize('monsters'))

'''
In each of the above cases we have handled one word. Now print the stemmed and lemmatised versions of all the words in the document  computerscience.txtPreview the document. Here is an overview of what you need to do: 

1. Load the file into a reader [ Hint: reader = WordListCorpusReader( ... ) ]
2. use word_tokenize from nltk.tokenize to convert the text into words
3. Loop through the text [Hint: Use the forLinks to an external site. statement]
4. Lemmatise and Stem each word.
5. Look at the difference between the two, notice how the lemmatiser makes mistakes in some cases - can you identify why and propose a solution?
'''

from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader('./', ['computerscience.txt'])
for count, ele in enumerate(reader.words()):
    print(count, "\b:", ele, "\n")