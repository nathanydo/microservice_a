import re
from datetime import datetime, timedelta
import time

def read_date_from_file():
    try:
        with open('workout_date.txt', 'r') as file:
            date_string = file.readline().strip()  # Read just the first line
            match = re.search(r'\d+-\d+-\d{4}', date_string)
            if match:
                # Parse as MM-DD-YYYY
                date_from_file = datetime.strptime(match.group(), '%m-%d-%Y').date()
                return date_from_file
    except (FileNotFoundError, ValueError, AttributeError):
        return None
    return None

def main():
    stored_date = None
    current_streak = 0

    while True:
        new_date = read_date_from_file()
        
        if new_date:
            if stored_date:
                # Compare with stored date
                if new_date == stored_date + timedelta(days=1):
                    current_streak += 1
                elif new_date == stored_date:
                    # Same date, do nothing
                    pass
                else:
                    current_streak = 1
            else:
                # Streak resets
                current_streak = 1
            
            stored_date = new_date
            
            # Write the streak to a file for main program to read
            with open('streak_results.txt', 'w') as streak_file:
                streak_file.write(str(current_streak))
            
            print(f"Current streak: {current_streak}")
        
        # Wait for 5 seconds before checking again (can lower the time if you want faster response)
        time.sleep(5)

if __name__ == "__main__":
    main()