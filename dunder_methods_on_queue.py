'''from queue import Queue
import inspect

q = Queue()
print(q) # Will give memory location, since queue does not have a __repr__ method

print(inspect.getsource(Queue))
'''

# If you want to make your own queue class, do this:
from queue import Queue as q
import inspect

class Queue(q):        # extends from q
    def __repr__(self):
        return f'Queue({self.qsize()})'

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get()

qu = Queue()
qu + 9
qu + 7
qu - 0
qu - None
print(qu)