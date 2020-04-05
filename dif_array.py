def array_diff(a, b):
    return [n for n in a if n not in b]

def array_diff2(a, b):
    c = set(a) - set(b)
    print(list(c))
    return c

print(array_diff([1,2,2,2,3,3], [2]))