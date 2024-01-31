class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added successfully.')

    def mark_as_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f'Task "{task}" marked as completed.')
                return
        print(f'Task "{task}" not found.')

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for index, t in enumerate(self.tasks, start=1):
                status = "Completed" if t["completed"] else "Not Completed"
                print(f'{index}. {t["task"]} - {status}')

# Example Usage:
todo_list = ToDo()

# Adding tasks
todo_list.add_task("Buy groceries")
todo_list.add_task("Finish report")
todo_list.add_task("Exercise")

# Displaying tasks
todo_list.display_tasks()

# Marking a task as completed
todo_list.mark_as_completed("Finish report")

# Displaying tasks after marking one as completed
todo_list.display_tasks()
