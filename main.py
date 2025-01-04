import requests
import os

api_key = os.environ['API_KEY']

def chat_with_bot(message, conversation_id=None):

    url = 'https://rockydore.com/chat'

    payload = {
        "message": message,
        "conversation_id": conversation_id or "",
    }

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes

        result = response.json()
        return result["response"], result["conversation_id"]

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None, None


def main():
    print("Chat with the interview bot (type 'quit' to exit)")

    response, conversation_id = chat_with_bot('')
    if response:
        print(f"\nInsito Bot: {response}")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            break

        response, conversation_id = chat_with_bot(user_input, conversation_id)
        if response == "__end__":
            break
        elif response:
            print(f"\nInsito Bot: {response}")
            if "(You died... Game over.)" in response or "Congratulations! You Won!" in response:
                # Break after printing response
                break


if __name__ == "__main__":
    main()
