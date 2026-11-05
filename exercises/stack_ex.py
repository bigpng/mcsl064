import math


# Exercise 11
class Stack:
    def __init__(self) -> None:
        self.items: list[object] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0  # Check if stack empty

    def push(self, item: object) -> None:
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.items.pop()

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


def stack(st: Stack) -> None:
    while True:
        option = int(input("Enter an operation: 1. Push;  2. Pop; 3. Peek;  4. Size;  0. Exit: "))
        match option:
            case 0:
                break
            case 1:
                num = input("Enter an element: ")
                st.push(num)
            case 2:
                print(st.pop())
            case 3:
                print(st.peek())
            case 4:
                print(st.size())
            case _:
                print("Invalid entry")


# Exercise 12
def evaluate_postfix(arr: list[str]) -> int:
    st = []
    for token in arr:
        if token[0].isdigit() or (len(token) > 1 and token[0] == "-"):
            st.append(int(token))
        else:
            val1, val2 = st.pop(), st.pop()

            match token:
                case "+":
                    st.append(val2 + val1)
                case "-":
                    st.append(val2 - val1)
                case "*":
                    st.append(val2 * val1)
                case "/":
                    st.append(val2 // val1)
                case "^":
                    st.append(int(math.pow(val2, val1)))
                case _:
                    print("Unsupported operand")
    return int(st.pop())
