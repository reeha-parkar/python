import inspect

'''x = [1, 2, 3]
y = [4, 5]

print(type(x)) # Output: <class 'list'>
# Whatever we make it print, it follows a certain pattern
# Which means that there is some class related method that works uunder the hood to give a certain output
'''
# Let's make our own data type:
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self): # a dunder/magic method that allows us to define object's string representation
        return f'Person({self.name})' 

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception('Invalid argument, must be type int')
        self.name = self.name * x

    def __call__(self, y):
        print('called this function', y)

    def __len__(self):
        return(len(self.name))
            

p = Person('tim')
p * 4
p(4) # When you call this function, __call__ will work
print(p) # this initially, prints the memory address location
# The dunder methods are a part of 'data model' of python
print(len(p))