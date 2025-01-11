'''
Write a program that simulates the way in which a user might choose a password. 
The program should prompt for a new password, and then prompt again. If the two 
passwords entered are the same the program should say "Password Set" or similar, 
otherwise it should report an error. 

'''

p1=input("Enter your new password: ")
p2=input("Enter your new password again: ")
if p1==p2:
    print("Password Set")
else:
    print("Error: Passwords do not match")