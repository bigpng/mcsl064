def calculate_total(price: int, quantity: int) -> int:
    total = price * quantity
    return total


def greet(name: str) -> str:
    message = "Hello, " + name
    return message


def get_first(items: list[str]) -> str:
    return items[0]


result = calculate_total(10, 5)
print(greet("123"))
print(get_first([]))
