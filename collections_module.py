import collections

'''
# Counter:
from collections import Counter
a = Counter('gallad')
print(a)
b = Counter(['a', 'a', 'b', 'b', 'c'])
print(b)
c = Counter({'a': 1, 'b': 2})
print(c)
d = Counter(cats=4, dogs=3)
print(d)
print(d['cats'])
print(d['pets']) # will give 0 and not an error, unlike dictionary

print(list(c.elements()))

print(c.most_common())   

x = Counter(a=4, b=2, c=0, d=-2)
y = Counter(['a', 'b', 'b', 'c'])
x.subtract(y)
print(x)
x.update(y)
print(x)

#x.clear() # Will clear the counter
#print(x)

# Other operations:
print(x+y)
print(x-y)
print(x&y) # minimum elements
print(x|y) # max elements
'''

'''# Named Tuple
from collections import namedtuple
Point = namedtuple('Point', 'x y z')
#oint = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0}) # works, but ignores the value, only takes key
newP = Point(1, 2, 3)
print(newP)

# All its methods require underscore before them
print(newP.x, newP.y, newP.z)
print(newP[0])
# Can convert it into dictionary, giver ordereddict
print(newP._asdict()) 
print(newP._fields)
newP = newP._replace(y=6) # needs to be assigned to a variable
print(newP)
p2 = Point._make(['a', 'b', 'c'])
print(p2)
'''

# Deque
from collections import deque
# list, but faster than a list to add an element at the start or at the end
d = deque('hello')
print(d)

d.append('4')
d.append(5)
d.appendleft(123)
d.pop()
d.popleft()
d.clear()
d.extend('456')
d.extend('hello')
d.extend([1, 2, 3])
d.extendleft('hey') # will get reverse order at the start
d.rotate(-1) # rotate by position 1, to the left (negative)
d.rotate(4)
#print(d)

e = deque('hello', maxlen=5)
print(e)
e.append(1)
print(e)
e.extend([1, 2, 3, 4])
print(e)
e.reverse()
print(e)
# cannot change the maxlen, but can only access it by:
print(e.maxlen)
