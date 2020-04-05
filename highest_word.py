def high(sentence):
    dict = {}
    arr = []
    for word in sentence.split():
        high = sum(ord(l) - 96 for l in word)
        if high not in dict:
            dict[high] = word
            arr.append(high)
    arr.sort()
    print(dict)
    return dict[arr[-1]]

def high2(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
        print(list)
    return words[list.index(max(list))]

a = ord('a')
for w in range(a, a + 26):
    print('{} {}'.format(chr(w), w ))


print(high('what time are we climbing up the volcano'))
print(high2('what time are we climbing up the volcano'))
