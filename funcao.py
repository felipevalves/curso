import string
name = input('Nome: ')

def myPrint(name):
    print('myPrint')
    print('Olá {}'.format(name.title()))
    print('Olá {}'.format(string.capwords(name)))

myPrint(name)

def multiply(a,b):
    a*b
print(multiply(1,2))

