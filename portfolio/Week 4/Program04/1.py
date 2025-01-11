def input(num):
    return num in range(0,100)

def input_test():
    values=[1,5,44,-33,22,-90,111,68]
    for value in values:
        result=input(value)
        print(f"Input {value} is validation: {result}")

input_test()
