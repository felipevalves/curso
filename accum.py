def accum(word):
    new_list = [(w * i).capitalize() for i, w in enumerate(word, start=1)]
    return '-'.join(new_list)

def accum2(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
print(accum('abcderg'))
print(accum2('abcderg'))

letter = 'a' * 2
print(letter.capitalize())