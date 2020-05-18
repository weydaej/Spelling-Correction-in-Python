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

# unigrams
from nltk.tag import UnigramTagger
unigram_tagger = UnigramTagger(train_sents)
tagger = UnigramTagger(train_sents, cutoff=3)
print(tagger.evaluate(test_sents))

# bigrams
from nltk.tag import BigramTagger
bigram_tagger = BigramTagger(train_sents)
tagger = BigramTagger(train_sents, cutoff=3)
print(tagger.evaluate(test_sents))

# trigrams
from nltk.tag import TrigramTagger
trigram_tagger = TrigramTagger(train_sents)
tagger = TrigramTagger(train_sents, cutoff=3)
print(tagger.evaluate(test_sents))

# backoff
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)
def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes:
        backoff = cls(train_sents, backoff=backoff)
    return backoff

tagger = backoff_tagger(train_sents, [UnigramTagger, BigramTagger, TrigramTagger], backoff=DefaultTagger('NN'))
print(tagger.evaluate(test_sents))
# this hits 88% accuracy