def last_char(string):
    if len(string)>1:
        return string[:-1]
    return string

print(last_char("Apple"))
print(last_char("A"))
print(last_char(""))