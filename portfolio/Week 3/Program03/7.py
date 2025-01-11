'''
Modify your "Times Table" program so that the user enters the number 
of the table they require. This number should be between 0 and 12 inclusive.
'''

num=int(input("Enter the number of the table you require: "))
if num<0 or num>12:
    print("Invalid input. Please enter a number between 0 and 12 inclusive.")
else:
    for i in range(13):
        prod=i*num
        print(i, 'x', num, '=', prod)
        i+=1