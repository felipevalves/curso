def dig_pow(n, p):
    numbers = list(str(n))
    total = 0
    for i in numbers:
        total += int(i) ** p
        p += 1

    k = int(total / int(n))

    if (n * k) == total:
        return k
    return -1

def dig_pow2(n, p):
    numbers = list(str(n))
    total = 0
    for i in numbers:
        total += int(i) ** p
        p += 1

    if total % n == 0:
        return total / n
    return -1

print('dig_pow: {}'.format(dig_pow2(46288, 3)))