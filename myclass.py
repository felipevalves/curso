class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print('Hello my name is {}'.format(self.name))

    def myFunc2(abc):
        print('myFunc 2 {}'.format(abc.name))

p1 = Person('Felipe', 34)

print('{} {} '.format(p1.name, p1.age))
p1.myFunc()
p1.myFunc2()

