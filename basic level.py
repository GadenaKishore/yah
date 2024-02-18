class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, description):
        for task in self.tasks:
            if task.description.lower() == description.lower():
                self.tasks.remove(task)
                print("Task removed successfully.")
                return
        print("Task not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. Description: {task.description}, Priority: {task.priority}")

    def prioritize_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)
        for task in sorted_tasks:
            print(f"Description: {task.description}, Priority: {task.priority}")

    def recommend_task(self):
        if not self.tasks:
            print("No tasks found.")
            return

        high_priority_tasks = [task for task in self.tasks if task.priority.lower() == 'high']
        if high_priority_tasks:
            print("Recommendation: Consider working on a high priority task.")
        else:
            print("Recommendation: You can choose any task.")

# Sample usage
task_manager = TaskManager()
task_manager.add_task("Buy groceries", "High")
task_manager.add_task("Complete project report", "Medium")
task_manager.add_task("Schedule a meeting with the team", "Low")
task_manager.add_task("Prepare presentation for the meeting", "Medium")
task_manager.add_task("Pay the bills", "High")
task_manager.add_task("Exercise", "Low")

task_manager.list_tasks()
print("\n---\n")
task_manager.prioritize_tasks()
print("\n---\n")
task_manager.recommend_task()
