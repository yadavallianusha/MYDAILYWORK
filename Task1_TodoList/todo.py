# Simple To-Do List Program
todo_list = []

while True:
    print("\n----- TO DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(i, task)

    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            try:
                num = int(input("Enter task number to remove: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if 1 <= num <= len(todo_list):
                removed_task = todo_list.pop(num - 1)
                print("Removed task:", removed_task)
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
