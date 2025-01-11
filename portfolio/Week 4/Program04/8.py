import statistics

def read_temperatures():
    """Read exactly 6 temperatures from the user."""
    temperatures = []
    print("Enter 6 temperatures:")
    for i in range(6):
        while True:
            user_input = input(f"Temperature {i + 1}: ")
            try:
                temp = float(user_input)
                temperatures.append(temp)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    return temperatures

def main():
    temperatures = read_temperatures()
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = statistics.mean(temperatures)

    print("\nTemperature Summary:")
    print(f"Maximum temperature: {max_temp:.2f}")
    print(f"Minimum temperature: {min_temp:.2f}")
    print(f"Mean temperature: {mean_temp:.2f}")

if __name__ == "__main__":
    main()