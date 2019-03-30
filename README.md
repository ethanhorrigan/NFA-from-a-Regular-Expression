
# NFA from a Regular Expression

A Python application which can build a non-deterministic finite automaton (NFA) from a regular expression.

## Getting Started

```
$ git clone https://github.com/ethanhorrigan/NFA-from-a-Regular-Expression.git
```

navigate inside the project within cmd and use this command
```
$ python.exe main.py
```

### Problem Statement

```
You must write a program in the Python programming language [2] that can
build a non-deterministic finite automaton (NFA) from a regular expression,
and can use the NFA to check if the regular expression matches any given
string of text. You must write the program from scratch and cannot use the
re package from the Python standard library nor any other external library.
A regular expression is a string containing a series of characters, some of
which may have a special meaning. For example, the three characters ., |,
and * have the special meanings concatenate, or, and Kleene star respectively.
For example, the regular expression 0.1 means a 0 followed by a 1, 0|1 means
a 0 or a 1, and 1* means any number of 1’s. These special characters must
be used in your submission.
Other special characters you might consider allowing as input are brackets
() which can be used for grouping, + which means at least one of, and ? which
means zero or one of. You might also decide to remove the concatenation
character, so that 1.0 becomes 10, with the concatenation implicit. You may
initially restrict the non-special characters your program works with to 0 and
1. However, you should at least attempt to expand these to all the digits,
and the characters a to z, and A to Z.
```


## Built With

* [Python (Anaconda)](https://www.anaconda.com/distribution/)


## Research

Converting a Regular Expression to an NFA
![alt text](https://github.com/ethanhorrigan/NFA-from-a-Regular-Expression/blob/master/research/RegularExpressionToNFA.PNG "Convert Regular Expression to NFA")

## Resoruces
Converting infix expressions to postfix expressions
- http://www.oxfordmathcenter.com/drupal7/node/628

Regular Expression Matching
- https://swtch.com/~rsc/regexp/regexp1.html

Python Dictionaries
- https://realpython.com/python-dicts/

I read some answers from this forum to further my understanding of the Shunting Yard Algorithm
- https://codereview.stackexchange.com/questions/201232/shunting-yard-algorithm

Infix, Prefix & Postfix expression
- http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html

## Authors

* **Ethan Horrigan** - *Developer* - [Ethan Horrigan](https://github.com/ethanhorrigan)

## Acknowledgments

* Ian McLoughlin's Video Tutorials on various Algorithms
* Various articles I read, links are under 'Resources'
