class _Private:       # a private class/method will have an underscore prior to its name
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):  # even after an underscore, can use this normally
        print('Hello')
        
    def display(self):
        print('Hi')