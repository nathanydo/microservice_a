# Workout Streak Microservice

## Communication Contract

This microservice calculates the workout streaks of the user. The main program will write into `workout_date.txt`, where the microservice will read and calculate if the user has a streak. It will then write the streak into `streak_results.txt`.

## Files

- `workout_date.txt`: Contains the dates of the user's workouts.
- `streak_results.txt`: Contains the calculated workout streaks.

## How to Request Data

To request data, write into workout_dates.txt:

- `workout_date.txt`:

  ```
  10-01-2023  # make sure date is formated as month-day-year
  ```

Example code:

```
with open('workout_date.txt', 'w') as file:
  file.write("7-20-2022")
```

## How to Recieve Data

To recieve data, read from streaks_results.txt

- `streak_result.txt

  ```
  1
  ```

Example code:

```
with open('streak_results.txt', 'r') as file:
  results = file.readline().strip()
```

## Setup Instruction

1. Clone files from git repository
2. Run microservice.py (python3 microservice.py)
3. Write into workout_results.txt and read from streak_results.txt

## UML Diagram

![DIAGRAM](<./UML%20Diagram(2).jpg>)

## Dependencies

- Python 3.x (or any other language used)
- Any required libraries (e.g., `datetime` for date handling)

## License

This project is licensed under the MIT License.
