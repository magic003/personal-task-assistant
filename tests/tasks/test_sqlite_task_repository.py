from datetime import datetime

import pytest

from tasks import SqliteTaskRepository, Task


def test_create_task(sqlite_task_repository: SqliteTaskRepository) -> None:
    with sqlite_task_repository:
        now = datetime.now()
        task = Task(title="Test Task 1", done=False, due_time=now)
        created_task = sqlite_task_repository.create_task(task)
        assert created_task.id is not None
        assert created_task.title == "Test Task 1"
        assert created_task.done is False
        assert created_task.due_time == now


def test_create_task_with_id(sqlite_task_repository: SqliteTaskRepository) -> None:
    with sqlite_task_repository:
        task = Task(
            id="custom-id-123",
            title="Test Task with ID",
            done=False,
            due_time=datetime.now(),
        )
        with pytest.raises(
            ValueError, match="Task ID should be None when creating a task."
        ):
            sqlite_task_repository.create_task(task)


def test_complete_task(sqlite_task_repository: SqliteTaskRepository) -> None:
    with sqlite_task_repository:
        task = Task(title="Test Task 2", done=False, due_time=datetime.now())
        created_task = sqlite_task_repository.create_task(task)

        assert created_task.id is not None
        result = sqlite_task_repository.complete_task(created_task.id)
        assert result is True

        tasks = sqlite_task_repository.list_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].done is True

        result = sqlite_task_repository.complete_task("custom-id-123")
        assert result is False


def test_list_all_tasks(sqlite_task_repository: SqliteTaskRepository) -> None:
    with sqlite_task_repository:
        tasks = sqlite_task_repository.list_all_tasks()
        assert len(tasks) == 0

        task1 = Task(title="Task 1", done=False, due_time=datetime.now())
        task2 = Task(title="Task 2", done=False, due_time=datetime.now())
        sqlite_task_repository.create_task(task1)
        sqlite_task_repository.create_task(task2)

        tasks = sqlite_task_repository.list_all_tasks()
        assert len(tasks) == 2
        titles = {task.title for task in tasks}
        assert titles == {"Task 1", "Task 2"}
