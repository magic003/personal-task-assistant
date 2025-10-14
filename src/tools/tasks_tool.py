from datetime import datetime

from tasks import Task, TaskRepository


class TasksTool:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def add_task(self, title: str, due_time: datetime) -> str:
        """Add a new task.

        Args:
            title (str): The title of the task.
            due_time (datetime): The due time of the task.

        Returns:
            str: The ID of the created task.
        """
        task = Task(title=title, done=False, due_time=due_time)
        created_task = self.task_repository.create_task(task)
        return str(created_task.id)
