from exam_prep.python_oop_exam_16_aug_2020.project import Task


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
        try:
            task = [task for task in self.tasks if task.name == task_name][0]
            task.completed = True
            return f"Completed task {task.name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        all_not_completed_tasks = [t for t in self.tasks if not t.completed]
        n_removed_tasks = len(self.tasks) - len(all_not_completed_tasks)
        self.tasks = all_not_completed_tasks
        return f"Cleared {n_removed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += f"{task.details()}\n"
        return result

