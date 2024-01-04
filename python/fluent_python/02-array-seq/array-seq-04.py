"""
Slicing
  [a:b:c]: used as indexing operator, generate a slice object slice(a,b,c)
  seq[start:stop:step], call seq.__get_item(slice(start, stop, step))

Augmented Assignment with Sequences
  += works with __iadd__: for mutable sequences, __iadd__ is implmented and += happens in place;
  for immutable sequences; += creates a new copy

"""

# Slice Objects
s = 'bicycle'
s[::3]
# 'bye'
s[::-1]
# 'elcycib'
s[::-2]
# 'eccb'


invoice = """
0.....6.................................40........52...55........
1909 Pimoroni PiBrella                      $17.50    3    $52.50
1489 6mm Tactile Switch x20                  $4.95    2    $9.90
1510 Panavise Jr. - PV-201                  $28.00    1    $28.00
1601 PiTFT Mini Kit 320x240                 $34.95    1    $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])
    # $17.50   imoroni PiBrella
    #  $4.95   mm Tactile Switch x20
    # $28.00   anavise Jr. - PV-201
    # $34.95   iTFT Mini Kit 320x240


# Assigning to Slices
l = list(range(10))
l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
l
# [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
l
# [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]
l
# [0, 1, 20, 11, 5, 22, 9]
# By design, this example raises an exception::
try:
    l[2:5] = 100
except TypeError as e:
    print(repr(e))
# TypeError('can only assign an iterable')
l[2:5] = [100]
l
# [0, 1, 100, 22, 9]


# Using + and * with Sequences
# my_list = [[]] * 3 result in a list with three reference to the same inner list
l = [1, 2, 3]
l * 5
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
5 * 'abcd'
# 'abcdabcdabcdabcdabcd'


# Building Lists of Lists
board = [['_'] * 3 for i in range(3)] # correct way
weird_board = [['_'] * 3] * 3 # wrong way


# Augmented Assignment with Sequences
l = [1, 2, 3]
idl = id(l)
l *= 2
id(l) == idl  # same list

t = (1, 2, 3)
idt = id(t)
t *= 2
id(t) == idt  # new tuple: False


# Bytecode for the expression s[a] += b
# import dis

# dis.dis('s[a] += b')
#   1           0 LOAD_NAME                0 (s)
#               2 LOAD_NAME                1 (a)
#               4 DUP_TOP_TWO
#               6 BINARY_SUBSCR
#               8 LOAD_NAME                2 (b)
#              10 INPLACE_ADD
#              12 ROT_THREE
#              14 STORE_SUBSCR
#              16 LOAD_CONST               0 (None)


# list.sort and the sorted Built-In Function
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
sorted(fruits, key=len, reverse=True)

fruits.sort()


# When a List Is Not the Answer
# Arrays: support all mutable sequence operations (including .pop, .insert, and .extend),
# as well as additional methods for fast loading and saving, as .frombytes and .tofile
from array import array
from random import random, seed
seed(10)  # Use seed to make the output consistent

floats = array('d', (random() for i in range(10 ** 7)))
floats[-1]

with open('floats.bin', 'wb') as fp:
    floats.tofile(fp)
floats2 = array('d')

with open('floats.bin', 'rb') as fp:
    floats2.fromfile(fp, 10 ** 7)

floats2[-1]

floats2 == floats


# Memory Views
octets = array('B', range(6))
m1 = memoryview(octets)
m1.tolist()

m2 = m1.cast('B', [2, 3])
m2.tolist()
# [[0, 1, 2], [3, 4, 5]]
m3 = m1.cast('B', [3, 2])
m3.tolist()
# [[0, 1], [2, 3], [4, 5]]
m2[1,1] = 22
m3[1,1] = 33
octets
# array('B', [0, 1, 2, 33, 22, 5])


# NumPy
import numpy as np

a = np.arange(12)
a
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
type(a)
# numpy.ndarray
a.shape
# (12,)
a.shape = 3, 4
a
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
a[2]
# array([ 8,  9, 10, 11])


# Deques and Other Queues
import collections

dq = collections.deque(range(10), maxlen=10)
dq
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.rotate(3)
dq
# deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6])
dq.rotate(-4)
dq
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
dq.appendleft(-1)
dq
# deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.extend([11, 22, 33])
dq
# deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33])
dq.extendleft([10, 20, 30, 40])
dq
# deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8])


# Soapbox
# Mixed bag lists
l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
try:
    sorted(l)
except TypeError as e:
    print(repr(e))
TypeError("'<' not supported between instances of 'str' and 'int'")
# Key is Brilliant
l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
sorted(l, key=int)
# [0, '1', 5, 6, '9', 14, 19, '23', 28, '28']
sorted(l, key=str)
# [0, '1', 14, 19, '23', 28, '28', 5, 6, '9']
