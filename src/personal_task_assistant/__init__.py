from google import genai

from agent import Agent
from tasks.sqlite_task_repository import SqliteTaskRepository

DB_FILE = "/tmp/tasks.sqlite"
MODEL = "gemini-2.5-flash"


def main() -> None:
    client = genai.Client()
    with SqliteTaskRepository(db_file=DB_FILE) as task_repository:
        agent = Agent(client=client, model=MODEL, task_repository=task_repository)
        agent.run()
