class Person:

    def __init__(self,name):
        self.name = name

    def whoami(self):
        return "you are " + self.name


p1 = Person('jegatheeswaran')
print(p1.whoami())
print(p1.name)
