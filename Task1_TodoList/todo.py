todo_list = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(i, task)

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        todo_list.pop(num - 1)
        print("Task removed!")

    elif choice == "4":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice")
