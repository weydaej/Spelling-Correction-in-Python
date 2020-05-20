import nltk
from nltk.corpus import ieer
docs = ieer.parsed_docs('NYT_19980315')
tree = docs[1].text
print(tree)