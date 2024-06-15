class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def view_tasks(self):
        if not self.tasks:
            print("To-Do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f'{i}. {task}')

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            completed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed from the to-do list.')
        else:
            print("Invalid task number.")

# Sample usage:
todo_list = ToDoList()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == '2':
        todo_list.view_tasks()
    elif choice == '3':
        task_number = int(input("Enter the task number to mark as completed: "))
        todo_list.mark_completed(task_number)
    elif choice == '4':
        task_number = int(input("Enter the task number to remove: "))
        todo_list.remove_task(task_number)
    elif choice == '5':
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
