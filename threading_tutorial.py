import threading
import time

'''
# Basic thread explanation with creating a single thread
def func():
    print('ran')
    time.sleep(1) # At this time, 2 will be printed, because concurrent
    print('done')
    time.sleep(1)
    print('now done')

x = threading.Thread(target=func)
x.start() # required to execute a thread

# Get the amount of active threads:
print(threading.activeCount()) # Will get 2, since there is this main thread and the one that we've created
time.sleep(1)
print('finally')
'''

'''
# Creating 2 threads:
def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)

for _ in range(2):
    x = threading.Thread(target=count, args=(10,)) # This creates our 2 threads
    x.start() 

print('Done')
'''

# Thread synchronization
ls = []

def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target=count, args=(5,))
x.start()  

x.join() # when this is below the y thread, o/p is [1,1,2,2,3,3,4,4,5,5]
 
y = threading.Thread(target=count2, args=(5,))
y.start()

y.join()

print(ls) # will give only [1,1] since while both of the threads sleep, it will run print from 3rd thread

# so we add x.join and y.join which tells that do not move ahead tuntil the thread finishes running