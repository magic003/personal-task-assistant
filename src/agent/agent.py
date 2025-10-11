from google import genai
from google.genai import types

from tools import current_time


class Agent:
    def __init__(self, client: genai.Client, model: str) -> None:
        self.client = client
        self.model = model

    def run(self) -> None:
        print("Welcome to personal task assistant! (type 'exit' to quit)\n")

        chat = self.client.chats.create(
            model=self.model,
            config=types.GenerateContentConfig(
                tools=[current_time],
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
