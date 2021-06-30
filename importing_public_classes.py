import public_and_private_classes
from public_and_private_classes import NotPrivate

test = NotPrivate('tim')
test.display() # Will give the public output
test._display() # Will still give the output from the private method

# So, in python, there is no such thing as private classes and public classes
# Only the fact that if there is a method or class with underscore preceding it, ine should not use it
