import string
from typing import Set


def ispangram(text: str, alphabet: str = string.ascii_lowercase) -> bool:
    """
    Returns True if the given text contains every letter of the alphabet at least once.
    """
    # Remove spaces and convert to lowercase
    cleaned_text: str = text.replace(" ", "").lower()

    # Convert strings to sets of characters
    text_characters: Set[str] = set(cleaned_text)
    alphabet_characters: Set[str] = set(alphabet)

    # Check if all alphabet letters are in the text
    return alphabet_characters.issubset(text_characters)


# Demo usage
if __name__ == "__main__":
    sentence: str = "The quick brown fox jumps over the lazy dog"
    result: bool = ispangram(sentence)
    print(f"Is pangram? {result}")