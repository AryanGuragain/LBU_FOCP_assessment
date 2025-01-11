'''
Modify your program a final time so that it executes until the user successfully chooses 
a password. That is, if the password chosen fails any of the checks, the program 
should return to asking for the password the first time. 

'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:     
    p1=input("Enter your new password: ")
    p2=input("Enter your new password again: ")
    if p1==p2:
        if len(p1)>=8 and len(p1)<=12:
            if p1 not in BAD_PASSWORDS:
                print("Password Set")
            else:
                print("Password is too common")
        else:
            print("Password must be 8-12 charcters")
    else:
        print("Error: Passwords do not match")