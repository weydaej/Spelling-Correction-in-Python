import nltk
grammar1 = nltk.CFG.fromstring(
    """
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my"
    N -> "man" | "dog" | "cat" | "telescope" | "park"
    P -> "in" | "on" | "by" | "with"
    """
)
print(grammar1)
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

# Parsing
sr_parser = nltk.ShiftReduceParser(grammar1)
sent = "Mary saw a dog".split()
for tree in sr_parser.parse(sent):
    tree.draw()