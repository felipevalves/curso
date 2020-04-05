# import string

def is_isogram(string):
    # return len(string) == len(set(string.lower()))
    mystring = string.replace(' ', '').upper()
    my_str = set(mystring.upper())
    # my_str = ''.join(set(mystring))
    return len(my_str) == len(mystring)





print(is_isogram('asd qwer zxc'))

