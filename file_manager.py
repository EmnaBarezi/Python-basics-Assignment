
FILE_NAME = "user_message.txt"

def save_message(message):
    """Write message to a text file and then print for confirmation, handling errors very well."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            f.write(message + "\n")
        print("Message saving was a success")
    except OSError as e:
        print(f"Error in saving message: {e}")

def read_message():
    """Read the saved message and print it, handling errors gracefully."""
    try:
        print("Reading saved message...")
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            content = f.read().rstrip("\n")
        print(content)
    except FileNotFoundError:
        print("message not found. Please save it first.")
    except OSError as e:
        print(f"Error reading message: {e}")
