from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in [task.name for task in self.tasks]:
            return f"Could not find task with the name {task_name}"
        task = [task for task in self.tasks if task.name == task_name][0]
        task.completed = True
        return f"Completed task {task.name}"

    def clean_section(self):
        cleared_tasks = 0
        for task in self.tasks:
            if task.completed:
                cleared_tasks += 1
                self.tasks.remove(task)

        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += f"{task.details()}\n"
        return result

