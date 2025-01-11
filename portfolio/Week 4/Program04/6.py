def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

temp=input("Enter a temperature in Celsius")

if temp[-1].upper()=='C':
    print(f"{celsius_to_fahrenheit(float(temp[:-1]))} F")
else:
    print("Invalid format")