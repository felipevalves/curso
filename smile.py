eyes = ':;'
nose = '-~'
mouth = ')D'


def count_smileys(arr):
    total = 0
    for s in arr:
        if len(s) == 2:
            total += valid_smile_without_nose(s)
        elif len(s) == 3:
            total += valid_smile_complete(s)

    return total


def valid_smile_without_nose(smile):
    if smile[0] in eyes and smile[1] in mouth:
        return 1
    return 0


def valid_smile_complete(smile):
    if smile[0] in eyes and smile[1] in nose and smile[2] in mouth:
        return 1
    return 0


print(count_smileys(['']))
