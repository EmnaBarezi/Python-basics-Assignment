
def validate_input(user_input):
    """Return True if user_input is a non-empty string after stripping whitespace."""
    return isinstance(user_input, str) and user_input.strip() != ""

def convert_to_binary(text):
    """
    Convert a string to 8-bit space-separated ASCII binary.
    If the text represents a number (e.g., an age), convert it to int and return Python's binary form using bin().
    """
    # If it's already an int, return bin directly
    if isinstance(text, int):
        return bin(text)

    # Try to treat it as a number first (for ages like "23")
    try:
        number = int(text)
        return bin(number)
    except (ValueError, TypeError):
        pass

    # Otherwise, treat it as a string of characters
    if not isinstance(text, str):
        text = str(text)
    return " ".join(format(ord(ch), '08b') for ch in text)

def create_message(name, age, name_binary, age_binary):
    """Return the full, user-friendly message block."""
    lines = [
        f"Hello {name}, you are {age} years old!",
        f"Name in binary: {name_binary}",
        f"Age in binary: {age_binary}",
    ]
    return "\n".join(lines)

