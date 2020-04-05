import re


def valid_parentheses(string):
    if string == '': return True

    s = [w for w in string if ord(w) == ord('(') or ord(w) == ord(')')]
    s = ''.join(s)
    print(s)
    if '()' not in s:
        return False
    return valid_parentheses(s.replace('()', ''))


line = 'syea(pikykha)()))f'
# line = 'ml(e()i)vlsl'
print('{} is valid? {}'.format(line, valid_parentheses(line)))

line = re.sub(r"\\()", "", line)
print(line)
