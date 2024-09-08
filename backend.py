import openai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

api_key = os.getenv("API_KEY")


class Chatbot:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def get_response(self, user_input):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",  # Updated model recommendation
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=3000,
            temperature=0.5
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    # Load your API key from a secure location (not directly in code)
    api_key = api_key
    chatbot = Chatbot(api_key)
    response = chatbot.get_response("Write a joke about birds.")
    print(response)