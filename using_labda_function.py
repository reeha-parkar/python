# Simple function that adds 5 to a value
def func(x):
    return x+5
print(func(2))

# Replacing that function with a lambda function:
# Lambda is used as long the expression in the function fits on line
func2 = lambda x: x+5
print(func2(9))

# Lambda is also used when you have to use a function inside a function
# So, you will not have to create another function
def func3(x):
    func4 = lambda x: x+5
    return func4(x) + 5
print(func3(5))

func5 = lambda x, y=4: x+y # also using optional parameters and double arguments
print(func5(2))

# Using lambda with the map and the filter function:
a = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map(lambda x: x+5, a)) # saves us from making another function
print(newList)

filteredList = list(filter(lambda x: x%2==0, a))
print(filteredList)