import statistics

def read_temperatures():
    """Read temperatures from the user until an empty input is given."""
    temperatures = []
    while True:
        user_input = input("Enter a temperature (or press Enter to finish): ")
        if user_input == "":
            break
        try:
            temp = float(user_input)
            temperatures.append(temp)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    return temperatures

def main():
    temperatures = read_temperatures()
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = statistics.mean(temperatures)

    print(f"Maximum temperature: {max_temp:.2f}")
    print(f"Minimum temperature: {min_temp:.2f}")
    print(f"Mean temperature: {mean_temp:.2f}")

if __name__ == "__main__":
    main()