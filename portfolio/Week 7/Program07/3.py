'''Write a program that manages a list of countries and their capital cities. It should prompt the user to enter the name of a country. If the program already "knows" the name of the capital city, it should display it. Otherwise it should ask the user to enter it. This should carry on until the user terminates the program (how this happens is up to you). 
Note: A good solution to this task will be able to cope with the country being entered variously as, for example, "Wales", "wales", "WALES" and so on. 
'''
def main():
    countries = {'France': 'Paris', 'Italy': 'Rome', 'UK': 'London'}
    
    while True:
        country = input("Enter the name of a country (or 'quit' to finish): ").strip()
        
        if country.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break
        
        country_name = country.capitalize()
        
        if country_name in countries:
            print(f"The capital of {country} is {countries[country_name].capitalize()}.")
        else:
            capital = input(f"What is the capital of {country}? ").strip()
            countries[country_name] = capital.capitalize()
            print(f"Thank you! I've added {country}'s capital as {capital.capitalize()}.")

main()