"""
Tuples As Records VS Are Not Just Immutable Lists

- Tuples used as records (unnamed)
- Tuples as Immutable Lists

To evaluate a tuple literal, Python compiler generates bytecode for a tuple constant
in one operation

Given a tuple t, tuple(t) simply returns a reference to the same t. There is no need to copy.
"""

# Tuples used as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)


for country, _ in traveler_ids:
    print(country)


# Tuples as Immutable Lists
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
a == b # True

b[-1].append(99) # (10, 'alpha', [1, 2, 99])
a == b # False


# an object is only hashable if its value cannot ever change.
# An unhashable tuple cannot be inserted as a dict key or a set element
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


tf = (10, 'alpha', (1, 2))  # Contains no mutable items
tm = (10, 'alpha', [1, 2])  # Contains a mutable item (list)
fixed(tf) # True
fixed(tm) # False
