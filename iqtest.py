def iq_test(numbers):
    my_numbers = numbers.split()

    par_numbers = list(filter(lambda a: int(a) % 2 == 0, my_numbers))
    impar_numbers = list(filter(lambda a: not int(a) % 2 == 0, my_numbers))

    if len(par_numbers) == 1:
        return my_numbers.index(par_numbers[0]) + 1
    elif len(impar_numbers) == 1:
        return my_numbers.index(impar_numbers[0]) + 1
    return -1

def iq_test2(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(1) == 1:
        return n.index(1)+1
    else:
        return n.index(0)+1

print(iq_test2(' 2 4 4 9 8'))