import re
def to_camel_case(text):
    words_ok = re.split('[_-]', text)
    return words_ok[0] + ''.join(w.capitalize() for w in words_ok[1:])



print((to_camel_case('the-stealth-warrior')))
