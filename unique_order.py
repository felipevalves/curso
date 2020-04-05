def unique_in_order(iterable):

    order = []
    for i, c in enumerate(iterable, start=0):
        if i == 0:
            order.append(c)
            continue
        if c != order[len(order) - 1]:
            order.append(c)

    print(order)
    pass

def unique_in_order2(iterable):
    if len(iterable) == 0: return []
    order = [iterable[0]]
    for c in iterable[1:]:
        print('{} {}'.format(order[-1], order[len(order) - 1]))
        if c != order[len(order) - 1]:
            order.append(c)

    return order



unique_in_order2('aaabbbccdd')