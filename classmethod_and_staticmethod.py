# class methods and static method:
# class method is a method in the class whcih takes te class name as a parameter, requires class instances
# static method is a method which can be directly called without creating an instance of the class

class Dog:
    dogs = []
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):   # cls means the name of the class
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for _ in range(n):
            print('Bark!')

'''
# Calling a classmethod:
tim = Dog('tim')
jim = Dog('jim')
print(Dog.dogs) # will get the Dog objects

print(tim.dogs) # will get the same 2 dog objects
print(Dog.num_dogs()) # will get 2
'''

# Calling a static method
Dog.bark(5)

# Only using the class name to get the method, without creating an instance

# Static method is used when you don't need self or an object of the class
# does not require a minimum parameter
# Class method takes the actual class and can access whatever is in the class
# requires a minimum one oarameter and that is 'cls'

