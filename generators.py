'''
# In such an example, we store all the values and then access them
# If there are so many values, there will be MemoryError
x = [i for i in range(10)]
for el in x:
    print(el)
'''

'''
# But you can use something like this, which will take each value and then print (one value at a time)
for i in range(10):
    print(i)
'''

'''
# Generator method:
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv

g = Gen(10)

while(True):
    try:
        print(next(g))
    except StopIteration:
        break 

'''  

# Using the yield keyword:
def gen(n):
    for i in range(n):
        yield i**2    # will pause the function, so we have all info of it
        # return will top the function

g = gen(100)
#for i in g:
#   print(i)
 
print(next(g))
print(next(g))
print(next(g))
print(next(g))
