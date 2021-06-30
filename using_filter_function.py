def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isOdd, a)) # will add the elements that satisfy the function to the b list
# So basically filters out the odd elemnts from a to b list
#print(a, b)

#c = list(map(add7, b)) # only adds 7 to the odd numbers
#print(c)

# Using map and filter together:
print(list(map(add7, filter(isOdd, a))))
