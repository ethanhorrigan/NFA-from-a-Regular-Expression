
# NFA from a Regular Expression

A Python application which can build a non-deterministic finite automaton (NFA) from a regular expression.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo


### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python (Anaconda)](https://www.anaconda.com/distribution/)

## Research

https://swtch.com/~rsc/regexp/regexp1.html

## Authors

* **Ethan Horrigan** - *Developer* - [Ethan Horrigan](https://github.com/ethanhorrigan)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
