# Spelling Correction in Python

Note: The following is based on Peter Norvig’s online blog post. However please do not just grab the code. The main point of the exercise is to get used to text processing in Python. I have intentionally not linked to the blog but will do so later in the term.

If you are new to Python - use this as an opportunity to slowly learn. It will be a challenge at first but we are sure you will learn very quickly.

### Introduction

Spelling Correction is a common task for most applications which deal with text. For example, most search engines will correct queries containing non-valid words. The best spelling correction algorithms use sophisticated models of common spelling errors. However we can achieve much using just lots of data. 

### Using lots of data for spelling correction

Suppose we have a misspelt word. It's likely that the word is only wrong by 1 or possibly two typos. Even so there are potentially many words it could be. For instance if I type "lates" then I might mean "late", "latest" or "lattes" etc. In such cases we try to find the correction c out of all the possible corrections  that maximizes the probability that c is the intended correction, given the original word w:

argmax<sub>c ∈ candidates</sub> P(c|w)

By [Bayes Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) this is equivalent to:

argmax<sub>c ∈ candidates</sub> P(c) P(w|c) / P(w)


But P(w) is constant to all candidates so we can ignore it.  We are left with choosing the maximum of the product of 

1. The probability of the correction occurring (without any consideration of context). This is the language model.

2. The probability of the word given the above correction. This is the error model.

Error models can be quite sophisticated. For instance it's far more common to duplicate letters or mistake "i" for "e". Below we'll ignore this and assume that errors due to just one mistake are far more likely than errors due to 2 but far less likely than words we actually have seen before.  

### Data

Under Data on this Canvas module, you'll find a file "bigtxt.zip" which is a zipped file containing lots of freely available (and copyright free) text. We'll use this to create a language model for calculating the probability of any word.

Specific Python Knowledge Required

[Basic String Manipulation](http://www.tutorialspoint.com/python/python_strings.htm)

[Regular Expressions](http://www.tutorialspoint.com/python/python_reg_expressions.htm)

[Sets](https://docs.python.org/3/tutorial/datastructures.html) (not needed but life is much easier if you do)

plus basic Python control structures such as loops & conditionals. Ask us for help!

The Counter data structure. 

Counter is a data structure contained in the "collections" module. Collections is a set of high performance data structures for big data. To use a Counter we need to :

``` >>> from collections import Counter ```

A Counter is a hashable dictionary which provides a count of how many times a "thing" occurs. For instance:

```
>>> def words(text): return re.findall(r'\w+', text.lower())
>>> WORDS = Counter(words(open('/.../big.txt').read()))
```

will create a dictionary lookup for the number of times every word occurs in big.txt. The function "words" uses a regular expression to transform all words in bigtxt to lowercase. 

Containers have a .value() method which generates a list of values

```>>> WORDS.values()```

These numbers are the number of times each word occurs in big.txt. 

```
>>> WORDS['a']
21124
```

Of course, big.txt also contains a lot of noise - including misspellings. However with enough data we can ignore such imperfections. 

### Procedure

1. write a function which calculates the probability of any word occurring in any context.

```
>>> P('the')
0.07154004401278254
>>> P('computer')
1.0756688194982902e-05
```

2. write a function which generates all one character edits from a given word.

```
>> edits1('cat')
{'cyat', 'cato', 'fat', 'cati', 'cate', 'czat', 'cgt', 'catv', 'cnt', 'cact', 'catc', 'caa', 'car', 'cax', 'cap', 'cmt', ... 'caot'}
```

> An edit can be defined as inserting, removing or changing one character or swapping two letters (e.g. "cmoputer"). You will note above my function returns a set. This is a nice data structure but you could also use a list (but it's less efficient since it will contain duplicates.)

3. write a function which all generates all two character edits from a given word.

> Hint: if you've done 2 then all you need to do is find all one character edits from the set of one character edits the function above returns. 

4. a function for checking which words are already known

> Given a string of length n there will be n deletions,  n-1 swaps, 26n alterations, and 26(n+1) insertions or 54n+25 possible candidates. This number becomes huge if we consider two edits. However we can shrink this set by only considering words we've already seen. 

5. a function which suggests candidate corrections for any misspelling.

> Any candidate must be 1) a word in big.txt 2) either 1 or 2 edits away from the misspelt word.

```
>>> candidates('th')
{'to', 'th', 'tu', 'oh', 'tt', 'ty', 'ti', 'ta', 'the', 'te', 'tm', 'ah', 'h', 't', 'tr', 'tz', 'thy', 'wh', 'eh', 'ch'}
```

> Note the above example - there's lots of noise. However probability theory will come to the rescue!

 

6. a function which pulls everything together - giving a misspelt word, it generates all possible corrections and chooses the most likely. 

```
>>> correction('cimputer')
'computer'
```

### More Advanced Work

The spelling corrector actually works fairly well - Norvig claims 75% accuracy on a corpus of spelling errors. More importantly it's relatively fast. However it's not without problems. Try:

```
>>> correction('reciet')
'recite'

>>> correction('adres')
'acres'
```

Contrary to our code, reciet is a common error for "receipt" and "adres" is commonly "address".  How can you improve the performance of the spelling corrector?
