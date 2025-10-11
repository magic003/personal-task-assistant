class TaskDB:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str) -> None:
        self.tasks.append(task)

    def get_tasks(self) -> list[str]:
        return self.tasks