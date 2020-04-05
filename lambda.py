def myfunc(n):
    return lambda a: a * n
mydouble = myfunc(2)

print(mydouble(10))