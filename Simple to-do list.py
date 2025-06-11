# Simple To-Do List App (console-based)

# The list to store tasks
tasks = []

# Show the menu
def show_menu():
    print("")
    print("To-Do List")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

# Main program loop
running = True
while running:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # View tasks
        if len(tasks) == 0:
            print("No tasks.")
        else:
            i = 0
            while i < len(tasks):
                print(str(i + 1) + ". " + tasks[i])
                i = i + 1
    
    elif choice == "2":
        # Add a task
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        print("Task added.")
    
    elif choice == "3":
        # Mark a task as done
        if len(tasks) == 0:
            print("No tasks.")
        else:
            i = 0
            while i < len(tasks):
                print(str(i + 1) + ". " + tasks[i])
                i = i + 1
            task_num = int(input("Enter task number to mark as done: "))
            if task_num >= 1 and task_num <= len(tasks):
                tasks[task_num - 1] = tasks[task_num - 1] + " (Done)"
                print("Task marked as done.")
            else:
                print("Invalid number.")
    
    elif choice == "4":
        # Delete a task
        if len(tasks) == 0:
            print("No tasks.")
        else:
            i = 0
            while i < len(tasks):
                print(str(i + 1) + ". " + tasks[i])
                i = i + 1
            task_num = int(input("Enter task number to delete: "))
            if task_num >= 1 and task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print("Deleted task: " + removed_task)
            else:
                print("Invalid number.")
    
    elif choice == "5":
        # Exit the program
        print("Goodbye!")
        running = False
    
    else:
        print("Invalid choice. Enter a number between 1 and 5.")
