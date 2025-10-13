from typing import Protocol

from tasks import Task


class TaskRepository(Protocol):
    def create_task(self, task: Task) -> Task:
        """Create a new task.

        Args:
            task (Task): The new task to create.

        Returns:
            Task: The task created in the repository.
        """
        ...

    def complete_task(self, id: str) -> bool:
        """Mark a task as completed.

        Args:
            id (str): The unique identifier of the task to complete.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        ...

    def list_all_tasks(self) -> list[Task]:
        """List all tasks in the repository.

        Returns:
            list[Task]: A list of all tasks.
        """
        ...
