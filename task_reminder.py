import datetime
import os

# Function to create a task reminder
def create_task_reminder(task, due_date):
    # Save the task and due date to a text file for storage
    with open('task_reminders.txt', 'a') as file:
        file.write(f"{task} - Due Date: {due_date}\n")
    print("Task reminder created successfully.")

# Function to list all task reminders
def list_task_reminders():
    if os.path.exists('task_reminders.txt'):
        with open('task_reminders.txt', 'r') as file:
            task_list = file.readlines()
            if task_list:
                print("Task Reminders:")
                for task in task_list:
                    print(task.strip())
            else:
                print("No task reminders found.")
    else:
        print("No task reminders found.")

# Example usage
while True:
    print("\nChoose an option:")
    print("1. Create Task Reminder")
    print("2. List Task Reminders")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        task = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        create_task_reminder(task, due_date)
    elif choice == '2':
        list_task_reminders()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
