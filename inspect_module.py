import inspect
from queue import Queue

def func(x):
    return x+5

#print(inspect.getsource(func))
print(inspect.getsource(Queue)) # can get all the functions in that module



