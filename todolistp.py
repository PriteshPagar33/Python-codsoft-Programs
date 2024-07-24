def display_menu():
    print("\n Pritesh To-Do List Menu")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nPritesh your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task(todo_list):
    task = input("\nEnter the task: ")
    todo_list.append(task)
    print("Task added successfully.")

def delete_task(todo_list):
    view_todo_list(todo_list)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("\nDear Pritesh, please Enter your choice (1-4): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            delete_task(todo_list)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
