'''
# Decorators: modify the behaviour of a function without actually changing the code

def func(string):
    def wrapper():
        print('Started')
        print(string)
        print('Ended')

    #return wrapper() # we return the wrapper function being called, so output: started hello ended
    return wrapper # Does not return any output, only memory location
x = func('hello')
print(x)

# To get output from <return wrapper> we call that function here:
x() # Now, it will give output

# This happens because functions in python are objects and we can call them
'''

'''
# Another way of playing with functions:
def func(f):
    def wrapper():
        print('Started')
        f()
        print('Ended')
    return wrapper

def func2():
    print('I am func2')

x = func(func2)
print(x)
x()

# Rather than doing the above 3 lines, we can:
func2 = func(func2) # This is not ideal, so we use decorators
func2()
'''

'''
#Using decorators, our code will look like this:
def func(f): # This is the way we write the function when we use decorators
    def wrapper():
        print('Started')
        f()
        print('Ended')
    return wrapper

@func
def func2():
    print('I am func2')

func2()

# The wrapper function and the all decorator-ed functions should have the same amount of arguments
# So, to solve this, we use unpacked operator (*args, **kwargs)
# def wrapper(*args, **kwargs), and even for f(*args, **kwargs)

# If we are returning a value in the decorator-ed function, 
# assign the f(*args, **kwargs) to a variable in the wrapper function
# and return that variable at the end of the wrapper function
'''

# TIMER DECORATOR:
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print('Time: ', total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(100000):
        pass

@timer
def test1():
    time.sleep(2)

test()
test1()