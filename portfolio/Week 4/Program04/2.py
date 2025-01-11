def upper_or_lower(string):
    uppercase=0
    lowercase=0
    for char in string:
        if char.isupper():
            uppercase+=1
        elif char.islower():
            lowercase+=1
        else:
            pass

    print(f"uppercase letters: {uppercase}")
    print(f"lowercase letters: {lowercase}")

upper_or_lower("Happy New Year")