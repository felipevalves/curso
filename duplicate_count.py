def duplicate_count(text):
    text = text.upper()
    list_text = list(set(text))
    total = 0
    for t in list_text:
        amount = text.count(t)
        if amount > 1:
            total += 1

    return total

def duplicate_count2(text):
    return len([t for t in set(text.upper()) if text.upper().count(t) > 1])


duplicate_count2('aabff')