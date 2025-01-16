import sys
import matplotlib.pyplot as plt
from tabulate import tabulate
import csv

def load_lap_data(file_path):
    """
    Lap data are loaded from a file and organized by Drivers ID

    file_path (str)is the path to the lap data file.

    If the specified file does not exist FileNotFoundError is shown

    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            race_title = lines[0].strip()
            lap_times = {} # Dictionary to store lap times for each driver
            for line in lines[1:]:
                driver_id = line[:3]
                lap_duration = float(line[3:])
                if driver_id not in lap_times:
                    lap_times[driver_id] = []
                lap_times[driver_id].append(lap_duration)
            return race_title, lap_times
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def save_results(race_title, driver_statistics, driver_details, file_name):
    """
    Save race results to a CSV file.

    race_title (str) is the title of the race.
    driver_statistics (dict)are statistics for each driver including fastest lap, 
                              average lap, and total laps.
    driver_details (dict) is a dictionary containing detailed information about each driver.
    file_name (str) is the name of the CSV file to save the results to.
    """

    headers = ["Driver ID", "Full Name", "Team", "Car Number", "Fastest Lap", "Average Lap", "Total Laps"]
    rows = [
        [
            driver,
            driver_details[driver]["full_name"],
            driver_details[driver]["team"],
            driver_details[driver]["car_number"],
            stats["quickest"],
            stats["average"],
            stats["total_laps"]
        ]
        for driver, stats in driver_statistics.items()
    ]

    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([race_title])  # Add race title as the first row
            writer.writerow(headers)  # Add headers
            writer.writerows(rows)  # Add driver statistics
        print(f"Race results saved to {file_name}")
    except Exception as e:
        print(f"Error saving race results to CSV: {e}")

def load_driver_details(file_path):
    """
    Loads driver details from a file into a dictionary.

    file_path (str)is the path to the driver details file.

    dict is a dictionary containing driver details keyed by driver ID.
    
    FileNotFoundError is shown if the specified file does not exist.
    """
    driver_details = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                driver_id, team_name, car_number, full_name = line.strip().split(',')
                driver_details[driver_id] = {
                    "team": team_name,
                    "full_name": full_name,
                    "car_number": car_number
                }
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    return driver_details

def evaluate_lap_data(lap_times):
    """
    Evaluates lap data to calculate statistics for each driver and determine the overall fastest lap.

    lap_times (dict)is a dictionary containing lap times for each driver.
    
    A tuple containing the overall fastest lap (driver ID, time) and a dictionary
           of driver statistics. is returned in this function
    """
    overall_fastest = None
    driver_statistics = {}
    for driver, times in lap_times.items():
        quickest_time = min(times)
        average_time = sum(times) / len(times)
        driver_statistics[driver] = {
            "quickest": quickest_time,
            "average": average_time,
            "total_laps": len(times),
        }
        if overall_fastest is None or quickest_time < overall_fastest[1]:
            overall_fastest = (driver, quickest_time)
    return overall_fastest, driver_statistics

def show_race_results(race_title, overall_fastest, driver_statistics, driver_details, file_name):
    """
    Display race results in a table format and save them to a file.

    race_title (str): The title of the race.
    overall_fastest (tuple): A tuple containing the driver ID and time for the fastest lap.
    driver_statistics (dict): Statistics for each driver.
    driver_details (dict): Detailed information about each driver.
    file_name (str): The name of the file to save the race results to.
    """
    print(f"\n{race_title}")
    print(f"Overall Fastest Lap: {overall_fastest[0]} - {overall_fastest[1]:.3f}")
    sorted_driver_statistics = sorted(driver_statistics.items(), key=lambda item: item[1]["quickest"])
    headers = ["Driver ID", "Full Name", "Team", "Car Number", "Fastest Lap", "Average Lap", "Total Laps"]
    table = [
        [driver, driver_details[driver]["full_name"], driver_details[driver]["team"], driver_details[driver]["car_number"], stats["quickest"], stats["average"], stats["total_laps"]]
        for driver, stats in sorted_driver_statistics
    ]
    print(tabulate(table, headers, tablefmt="grid"))
    
    # Save the results to a specific CSV file
    save_results(race_title, driver_statistics, driver_details, file_name)

def plot_driver_statistics(driver_code, lap_times, driver_details):
    """
    Plot lap times for a specific driver.
    """
    if driver_code in lap_times:
        laps = list(range(1, len(lap_times[driver_code]) + 1))
        times = lap_times[driver_code]
        details = driver_details[driver_code]
        
        plt.figure(figsize=(10, 6))
        plt.plot(laps, times, marker='o', linestyle='-', color='b', label='Lap Times')
        plt.axhline(y=min(times), color='g', linestyle='--', label=f"Fastest Lap: {min(times):.3f}")
        plt.axhline(y=sum(times)/len(times), color='r', linestyle='--', label=f"Average Lap: {sum(times)/len(times):.3f}")
        
        plt.title(f"Lap Times for {details['full_name']} ({details['team']})")
        plt.xlabel("Lap Number")
        plt.ylabel("Lap Time (seconds)")
        plt.legend()
        plt.grid()
        plt.show()
    else:
        print(f"Error: Driver with code '{driver_code}' not found in the lap data.")

def find_driver_statistics(driver_code, driver_statistics, driver_details, lap_times):
    """
    Display statistics for a specific driver and optionally plot their lap times.
    """
    while driver_code not in driver_statistics:
        print(f"Error: Driver with code '{driver_code}' not found in the lap data.")
        driver_code = input("Please enter a valid driver code: ").strip().upper()
    
    stats = driver_statistics[driver_code]
    details = driver_details[driver_code]
    print(f"\nStatistics for Driver: {driver_code}")
    print(f"Full Name: {details['full_name']}")
    print(f"Team: {details['team']}")
    print(f"Car Number: {details['car_number']}")
    print(f"Fastest Lap: {stats['quickest']:.3f}")
    print(f"Average Lap: {stats['average']:.3f}")
    print(f"Total Laps: {stats['total_laps']}")
    
    # Ask if the user wants to see a graph
    show_graph = input("Do you want to see a graph of the lap times? (yes/no): ").strip().lower()
    if show_graph == "yes":
        plot_driver_statistics(driver_code, lap_times, driver_details)

def process_race_files(file_paths, driver_details):
    """
    Process multiple race files and display results.
        file_paths (list): List of file paths containing race data.
        driver_details (dict): Dictionary containing driver details.
    """
    race_to_file_map = {
        "Dewsberry": "dewsberry.csv",
        "Dewsberry 2": "dewsberry_2.csv",
        "York": "york.csv"
    }
    
    for file_path in file_paths:
        print(f"\nProcessing file: {file_path}")
        race_title, lap_times = load_lap_data(file_path)
        
        # Determine the output file based on race title
        output_file = race_to_file_map.get(race_title, f"{race_title.replace(' ', '_').lower()}_results.csv")
        
        overall_fastest, driver_statistics = evaluate_lap_data(lap_times)
        show_race_results(race_title, overall_fastest, driver_statistics, driver_details, output_file)

        driver_code = input("\nEnter a driver code to view their statistics (or press Enter to skip): ").strip()
        while driver_code:
            find_driver_statistics(driver_code, driver_statistics, driver_details, lap_times)
            driver_code = input("\nEnter another driver code to view their statistics (or press Enter to skip): ").strip()

if __name__ == "__main__":
    """
    Main entry point of the program.
    This script processes race files and displays detailed driver statistics.

    Usage:
        python timing_board.py <driver_details_file> <race_file1> <race_file2> <race_file3]
    """
    if len(sys.argv) < 3:
        print("Error: Missing required input files.")
        sys.exit(1)

    drivers_file_path = sys.argv[1]
    race_file_paths = sys.argv[2:]

    driver_details = load_driver_details(drivers_file_path)
    process_race_files(race_file_paths, driver_details)