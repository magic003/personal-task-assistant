from google import genai
from google.genai import types

from tasks.task_repository import TaskRepository
from tools import TasksTool, current_time


class Agent:
    def __init__(
        self, client: genai.Client, model: str, task_repository: TaskRepository
    ) -> None:
        self.client = client
        self.model = model
        self.task_repository = task_repository
        self.tasks_tool = TasksTool(task_repository)

    def run(self) -> None:
        print("Welcome to personal task assistant! (type 'exit' to quit)\n")

        chat = self.client.chats.create(
            model=self.model,
            config=types.GenerateContentConfig(
                tools=[current_time, self.tasks_tool.add_task],
                automatic_function_calling=types.AutomaticFunctionCallingConfig(
                    disable=False
                ),
                thinking_config=types.ThinkingConfig(
                    thinking_budget=0
                ),  # Disables thinking
            ),
        )

        while True:
            user_input = input("\u001b[94mYou\u001b[0m: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            response = chat.send_message(user_input)
            print("\u001b[92mAssistant\u001b[0m:", response.text)
