import string
from typing import Any


# Exercise 5: Recursive
def _compute_word_frequency_recursive(words: list[str]) -> dict[str, int]:
    def count_from(index: int, freq_dict: dict[str, int]) -> dict[str, int]:
        if index == len(words):  # Base case
            return freq_dict

        word = words[index]
        freq_dict[word] = freq_dict.get(word, 0) + 1
        return count_from(index + 1, freq_dict)  # The function calls itself with increased index

    return count_from(0, {})  # Starts the recursive process


def compute_word_frequency_recursive(text: str) -> dict[str, int]:
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")

    return _compute_word_frequency_recursive(text.split())


# Exercise 6
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)


# Not recursive
def factorial_loop(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


# Exercise 8
def reverse_string_recursive(text: str) -> str:
    if len(text) <= 1:
        return text

    return reverse_string_recursive(text[1:]) + text[0]


# Exercise 7: Iterative
def fibonacci(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n must be non-negative")
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib


# Exercise 7: Recursive
def fibonacci_recursive(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n must be non-negative")

    def build(rem: int, a: int, b: int, numbers: list[int]) -> list[int]:
        if rem == 0:
            return numbers  # Base case

        numbers.append(a)
        return build(rem - 1, b, a + b, numbers)  # Updated values

    return build(n, 0, 1, [])  # Initial call


# Exercise 9
def product_recursive(a: int, b: int) -> int:
    if b == 0:
        return 0  # Base case
    elif b < 0:
        return -product_recursive(a, -b)

    return a + product_recursive(a, b - 1)


def division_recursive(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    if a == 0:
        return 0
    elif b < 0:
        return -division_recursive(a, -b)
    elif a < 0:
        return -division_recursive(-a, b)

    if a < b:
        return 0  # Base case: if the dividend is smaller than the divisor, it fits 0 times

    return 1 + division_recursive(a - b, b)


# Exercise 10
def generate_subsets(elements: list[Any]) -> list[Any]:
    if not elements:
        return [[]]

    first = elements[0]
    rest_subsets = generate_subsets(elements[1:])

    with_first = [[first] + subset for subset in rest_subsets]

    return rest_subsets + with_first
