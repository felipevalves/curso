import itertools
def permutations(word):
    p = itertools.permutations(word, len(word))
    return [''.join(w) for w in list(set(p))]

print(permutations('aabb'))