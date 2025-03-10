import time

def write_dates():
    with open('workout_date.txt', 'w') as file:
        print("Writing to file: 7-20-2022")
        file.write("7-20-2022\n")
    time.sleep(2)
    with open('workout_date.txt', 'w') as file:
        print("Writing to file: 7-21-2022")
        file.write("7-21-2022\n")
    time.sleep(2)
    with open('workout_date.txt', 'w') as file:
        print("Writing to file: 7-22-2022")
        file.write("7-22-2022\n")

def read_streak():
    with open('streak_results.txt', 'r') as output:
        streak = output.readline().strip()
        print(f"\n\nCurrent Streak: {streak}")

def main():
    write_dates()
    time.sleep(2)
    read_streak()

if __name__ == "__main__":
    main()