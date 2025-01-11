'''Modify your greeting program so that if the user does not enter a name 
(i.e. they just press enter), the program responds "Hello, Stranger!". Otherwise
it should print a greeting with their name as before. 
'''

name=str(input("Hello, what is your name? "))
if name=="":
    print("Hello stranger")
else:
    print(f"Hello, {name}. Good to meet you!" )
