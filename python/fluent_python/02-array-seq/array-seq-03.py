"""
Sequence unpacking and sequence patterns

edge cases:
  [record] with only one record in list
  (record,) with only one record in tuple

- Sequence unpacking
- Pattern Matching with Sequences
    - Instances of str, byte, and bytearray are not handled as sequences in the context of match/case
    - Unlike unpacking, patterns do NOT destructure iterables that are not sequences (e.g., iterators)
    - case [name, _, _, (lat, lon) as coord]: # bind any part of a pattern with a variable using the as keyword
    - case [name, *_, (float(lat), float(lon))]:
"""

# -- Sequence unpacking --
# Using * to grab excess items
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # unpacking
latitude

t = (20, 8)
divmod(*t) # (2, 4)
quotient, remainder = divmod(*t)

import os
_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
filename

a, b, *rest = range(5)
a, b, rest # (0, 1, [2, 3, 4])

a, b, *rest = range(2)
a, b, rest # (0, 1, [])

a, *body, c, d = range(5)
a, body, c, d # (0, [1, 2], 3, 4)

*head, b, c, d = range(5)
head, b, c, d # ([0, 1], 2, 3, 4)


# Unpacking with * in function calls and sequence literals
def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


fun(*[1, 2], 3, *range(4, 7)) # (1, 2, 3, 4, (5, 6))
*range(4), 4 # (0, 1, 2, 3, 4)
[*range(4), 4] # [0, 1, 2, 3, 4]
{*range(4), 4, *(5, 6, 7)} # {0, 1, 2, 3, 4, 5, 6, 7}


# -- Pattern Matching with Sequences --
# match/case sequence handlings
# sequence pattern can be tuples or lists or any combination of nested tuples and lists.
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
main()
#                 |  latitude | longitude
# Mexico City     |   19.4333 |  -99.1333
# New York-Newark |   40.8086 |  -74.0204
# São Paulo       |  -23.5478 |  -46.6358


# Instances of str, byte, and bytearray are not handled as sequences in the context of match/case
# match tuple(phone):
#     case ['1', *rest]:
#         ...
#     case ['2', *rest]:
#         ...
#     case ['3' | '4', *rest]:
#         ...
