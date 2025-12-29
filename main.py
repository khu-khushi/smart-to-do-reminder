
import csv
import time
import threading

FILE_NAME = "tasks.csv"

# Function to add a task
def add_task(name, hours, minutes):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, hours, minutes])
    print(f"Task '{name}' added for {hours}:{minutes} ✅")

# Function to view tasks
def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            tasks = list(reader)
            if not tasks:
                print("No tasks yet ❌")
            else:
                print("\nTasks List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task[0]} at {task[1]}:{task[2]}")
    except FileNotFoundError:
        print("No tasks yet ❌")

# Function to check reminders in background
def check_reminders():
    while True:
        try:
            with open(FILE_NAME, "r") as file:
                reader = csv.reader(file)
                tasks = list(reader)
                for task in tasks:
                    name, hour, minute = task
                    hour = int(hour)
                    minute = int(minute)
                    current_time = time.localtime()
                    if current_time.tm_hour == hour and current_time.tm_min == minute:
                        print(f"\n⏰ Reminder: {name} NOW!")
                        print("\a")  # beep sound
                        time.sleep(60)  # wait 1 minute so it doesn't repeat immediately
            time.sleep(20)  # check every 20 seconds
        except FileNotFoundError:
            time.sleep(20)

# Start reminder thread
reminder_thread = threading.Thread(target=check_reminders, daemon=True)
reminder_thread.start()

# Main menu loop
while True:
    print("\nSmart To-Do Reminder System")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Task name: ")
        hours = input("Hour (0-23): ")
        minutes = input("Minute (0-59): ")
        add_task(name, hours, minutes)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice ❌")






