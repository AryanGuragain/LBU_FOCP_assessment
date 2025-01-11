'''
Modify your previous program so that the password must 
be between 8 and 12 characters (inclusive) long. 

'''
p1=input("Enter your new password: ")
p2=input("Enter your new password again: ")
if p1==p2:
    if len(p1)>=8 and len(p1)<=12:
        print("Password Set")
    else:
        print("Password must be 8-12 charcters")