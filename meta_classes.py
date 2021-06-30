# Do not use them in your code, ideally
# Use only when you absolutely need it

# In python, you can create a class within  function, because python will not give any error
# Because classes are actually objects, so it will be translated/interpreted in runtime
# A class creates an object for us, but it is by itself also an object
'''
def hello():
    class Hi:
        pass

    return Hi
'''

# A metaclass defines the rules of the class

'''
class Test:
    pass

print(Test)
print(Test())
print(type(Test())) # Output: <class '__main__.Test'>
print(type(Test)) # Output: <class 'type'>
# This gives class type, that means the type class is the metaclass that will define the Test class

class Foo:
    def show(self):
        print('hi')

def add_attribute(self):
    self.z = 9

# So, we can define the Test class like this:
Test2 = type('Test2', (Foo, ), {'x': 5, 'add_attribute': add_attribute}) # Class_name = type(name, any parent that we inherit from, attribute)

t = Test2()
print(t.x)
# can add attributes:
t.w = 'hello'
print(t.w)
# inherited method:
t.show()
# add a function in the class
t.add_attribute()
print(t.z)
'''

# Now we will define our own meta class:

class Meta(type): # will inherit from the class 'type'
    def __new__(self, class_name, bases, attrs):         # called before the init method, can modify the way object can be constructed
        print(attrs)
        a = {}
        for name, value in attrs.items():
            if name.startswith('__'):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print('hi')

d = Dog()
print(d.X) # d.x will give an error
# This is because we have changed it in meta class itself

# You can have metaclass that inherits other meta classes

