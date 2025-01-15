'''Write a function that accepts a positive integer as a parameter and then returns
 a representation of that number in binary (base 2).'''


def binary(num):
    if num<0:
        print("The value must be positive")
    binary_num=bin(num)[2:]
    return binary_num

print(binary(99))