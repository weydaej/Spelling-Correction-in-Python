# POS Taggers
# module load python/3.5
# brown and treebank corpora

from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]

# my first tagger
from nltk.tag import DefaultTagger
tagger = DefaultTagger('NN')
print(tagger.tag_sents([['Hello','.'],['My','name','is','Steve']]))
print(tagger.evaluate(test_sents))
