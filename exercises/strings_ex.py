import re
import string


# Execise 1
def analyse_string(text: str) -> tuple[int, int, int]:
    chars = len(text)
    blanks = text.count(" ")
    words = len(text.split())
    return chars, blanks, words


# Exercise 2
def remove_multiple_blanks(text: str) -> str:
    return re.sub(r" +", " ", text)


# Exercise 3
def reverse_string(text: str) -> str:
    return text[::-1]


# Exercise 4
def toggle_case(text: str) -> str:
    return text.swapcase()


# Exercise 5
def compute_word_frequency(text: str) -> dict[str, int]:
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()
    frequency_dict: dict[str, int] = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict
