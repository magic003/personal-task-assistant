from google import genai


class Agent:
    def __init__(self, client: genai.Client) -> None:
        self.client = client

    def run(self) -> None:
        print("Welcome to personal task assistant! (type 'exit' to quit)\n")

        while True:
            user_input = input("\u001b[94mYou\u001b[0m: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
