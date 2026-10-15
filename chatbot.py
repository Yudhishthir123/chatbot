
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY missing. Please check your .env file."
    )

client = OpenAI(api_key=api_key)


def ask_gpt(message):
    """Send user message to OpenAI and return the reply."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content


def main():
    print("GPT Chatbot is running!")
    print("Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() == "bye":
                print("Bot: Goodbye!")
                break

            if not user_input:
                print("Bot: Please enter a message.\n")
                continue

            reply = ask_gpt(user_input)
            print(f"Bot: {reply}\n")

        except KeyboardInterrupt:
            print("\nBot: Goodbye!")
            break

        except Exception as error:
            print(f"Bot: Something went wrong: {error}\n")


if __name__ == "__main__":
    main()
