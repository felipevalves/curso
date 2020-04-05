def order(sentence):
    my_sentence = sentence.split()
    numbers = range(1, len(my_sentence) + 1)
    s = []
    for i in numbers:
        s += [w for w in my_sentence if str(i) in w]

    return ' '.join(s)

def order2(words):
  return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))

print(order('is2 Thi1s T4est 3a'))
print(order2('is2 Thi1s T4est 3a'))
