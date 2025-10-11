from google import genai

from agent import Agent


def main() -> None:
    client = genai.Client()
    agent = Agent(client=client, model="gemini-2.5-flash")
    agent.run()
