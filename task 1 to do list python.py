  # To-do list program in Python

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nYour To-Do List is empty.")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task you want to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []  # This will hold the list of tasks
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
