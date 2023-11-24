from collections import namedtuple
def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)

# Use as namedtuple
p = profile()
print(p, type(p))
# https://book.pythontips.com/en/latest/global_&_return.html


# Person(name='Danny', age=31) <class '__main__.Person'>
print(p.name)
# Danny
print(p.age)
#31

# Use as plain tuple
p = profile()
print(p[0])
# Danny
print(p[1])
#31

# Unpack it immediatly
name, age = profile()
print(name)
# Danny
print(age)
#31