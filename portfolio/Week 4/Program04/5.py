def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

c_to_f=(celsius_to_fahrenheit(99))
f_to_c=(fahrenheit_to_celsius(36))
print(f"{c_to_f:.2f}")
print(f"{f_to_c:.2f}")