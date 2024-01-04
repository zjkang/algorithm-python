"""
List Comprehensions and Generator Expressions

built-in sequences
- container sequences: list, tuple, collections.deque
- flat sequences: str, bytes, array.array

memory diagram for tuple and array (Figure 2-1, page 23)

- mutable sequences: list, bytearray, array.array, collections.deque
- immutable sequences: tuple, str, bytes

Built-in concrete sequence types do not subclass the Sequence and MutableSequence
abstract base classes (ABCs), but they are virtual subclasses, rigistered with those ABCs
(Chapter 13)

List Comprehensions

Generator Expressions
save memory because it yields items one by one using iterator protocol instead of
building a whole list just to feed another constructor

https://github.com/fluentpython/example-code-2e/tree/master/02-array-seq
https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
"""

from collections import abc
issubclass(tuple, abc.Sequence) # True
issubclass(list, abc.MutableSequence) # True

import array
a=array.array('d',[1,2,3])
# >>> a
# array('d', [1.0, 2.0, 3.0])


symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
codes

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
codes

# assignment expression (walnut operator)
codes = [last := ord(c) for c in x]
last

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts


# Initializing a tuple and an array from a generator expression
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)

import array
array.array('I', (ord(symbol) for symbol in symbols))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
