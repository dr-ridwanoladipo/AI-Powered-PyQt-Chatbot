import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
api_key = os.getenv("API_KEY")


class Chatbot:
    """
    A class to interact with the OpenAI API for generating chat responses.
    """

    def __init__(self, api_key):
        """
        Initialize the Chatbot with an OpenAI API key.

        :param api_key: str, The OpenAI API key for authentication
        """
        self.client = OpenAI(api_key=api_key)

    def get_response(self, user_input):
        """
        Generate a response to the user's input using the OpenAI API.

        :param user_input: str, The user's input message
        :return: str, The generated response from the AI model
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the GPT-3.5 Turbo model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Set the AI's role
                {"role": "user", "content": user_input}  # User's input message
            ],
            max_tokens=150,  # Limit the response length
            temperature=0.5  # Control the randomness of the output (0.5 is balanced)
        )
        return response.choices[0].message.content  # Extract and return the generated text


# Example usage
if __name__ == "__main__":
    chatbot = Chatbot(api_key)
    response = chatbot.get_response("Write a joke about birds.")
    print(response)