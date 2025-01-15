num=int(input("Enter a number:"))
if num == 1:
    print("The number is not prime")
    
for i in range(2, num):
    if num % i == 0:
        print("The number is not prime")
        break
    else:
        print("The number is prime")
        break