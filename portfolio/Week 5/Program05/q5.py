import sys

def process_temperatures(temperatures):
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print(f"Maximum Temperature: {max_temp}")
    print(f"Minimum Temperature: {min_temp}")
    print(f"Mean Temperature: {mean_temp:.2f}")

def main():
    if len(sys.argv) < 2:
        print("No temperature readings provided. Please provide values as command-line arguments.")
        return

    try:
        temperatures = [float(arg) for arg in sys.argv[1:]]
        process_temperatures(temperatures)
    except ValueError:
        print("Error: All temperature readings must be numeric values.")

if __name__ == "__main__":
    main()