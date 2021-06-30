# Used when we are using list and then for loops for them:
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x**x

print(list(map(func, li))) # Applies the function func to every element in the list li

# Another way: list comorehension
print([func(x) for x in li])
# or maybe like this, to get selectve output:
print([func(x) for x in li if x%2 == 0])

