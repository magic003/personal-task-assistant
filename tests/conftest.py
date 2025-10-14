from pathlib import Path

import pytest

from tasks import SqliteTaskRepository


@pytest.fixture
def sqlite_task_repository(tmp_path: Path) -> SqliteTaskRepository:
    db_file = tmp_path / "test_tasks.sqlite"
    return SqliteTaskRepository(db_file=str(db_file))
