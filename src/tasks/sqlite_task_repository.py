import sqlite3
import uuid
from datetime import datetime

from tasks import Task, TaskRepository


class SqliteTaskRepository(TaskRepository):
    """A SQLite based task repository."""

    def __init__(self, db_file: str) -> None:
        self.db_file = db_file
        self._connect()
        self._create_table()

    def create_task(self, task: Task) -> Task:
        if task.id is not None:
            raise ValueError("Task ID should be None when creating a task.")
        task.id = str(uuid.uuid4())

        insert_sql = """
        INSERT INTO tasks (id, title, done, due_time)
        VALUES (?, ?, ?, ?);
        """
        try:
            self.cursor.execute(
                insert_sql,
                (task.id, task.title, int(task.done), task.due_time.isoformat()),
            )
            self.conn.commit()
            return task
        except sqlite3.Error as e:
            print(f"Error inserting task into database: {e}, task: {task.model_dump()}")
            raise

    def complete_task(self, id: str) -> bool:
        update_sql = """
        UPDATE tasks
        SET done = 1
        WHERE id = ?;
        """
        try:
            self.cursor.execute(update_sql, (id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error marking task as done in database: {e}, task id: {id}")
            return False

    def list_all_tasks(self) -> list[Task]:
        select_sql = """
        SELECT id, title, done, due_time
        FROM tasks;
        """
        try:
            self.cursor.execute(select_sql)
            rows = self.cursor.fetchall()
            tasks = [
                Task(
                    id=row[0],
                    title=row[1],
                    done=bool(row[2]),
                    due_time=datetime.fromisoformat(row[3]),
                )
                for row in rows
            ]
            return tasks
        except sqlite3.Error as e:
            print(f"Error listing all tasks from database: {e}")
            return []

    def disconnect(self) -> None:
        if self.conn:
            self.conn.close()

    def _connect(self) -> None:
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database in file {self.db_file}: {e}")

    def _create_table(self) -> None:
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0 CHECK (done IN (0, 1)),
            due_time TEXT NOT NULL
        );
        """
        try:
            self.cursor.execute(create_table_sql)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tasks table: {e}")
