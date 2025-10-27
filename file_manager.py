
FILE_NAME = "user_message.txt"

def save_message(message):
    """Write message to a text file and print confirmation, handling errors gracefully."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            f.write(message + "\n")
        print("Message saved successfully.")
    except OSError as e:
        print(f"Error saving message: {e}")

def read_message():
    """Read the saved message and print it, handling errors gracefully."""
    try:
        print("Reading saved message...")
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            content = f.read().rstrip("\n")
        print(content)
    except FileNotFoundError:
        print("No saved message found. Please save a message first.")
    except OSError as e:
        print(f"Error reading message: {e}")
