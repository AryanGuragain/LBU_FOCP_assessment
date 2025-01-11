'''Modify the "Times Table" again so that the user still enters the number of the table, 
but if this number is negative the table is printed backwards. 
So entering "-7" would produce the Seven Times Table starting at "12 times" down to "0 times".'''

num=int(input("Enter the number of the table you require: "))
if num<0:
    for i in range(12, -1, -1):
        prod=i*num
        print(i, 'x', num, '=', prod)
else:
    for i in range(13):
        prod=i*num
        print(num, 'x', i, '=',prod)
        i+=1

