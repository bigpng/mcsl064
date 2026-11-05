from textwrap import dedent

from exercises.binary_tree_ex import BinaryTree, binary_tree
from exercises.linked_list_ex import DoublyLinkedList, LinkedList, doubly_linked_list, linked_list
from exercises.queue_ex import IDeque, Queue, Queue2, ideque, iqueue, iqueue2
from exercises.recursive_ex import (
    compute_word_frequency_recursive,
    division_recursive,
    fibonacci,
    fibonacci_recursive,
    generate_subsets,
    product_recursive,
)
from exercises.stack_ex import Stack, evaluate_postfix, stack
from exercises.strings_ex import (
    analyse_string,
    remove_multiple_blanks,
    reverse_string,
    toggle_case,
)


def main() -> None:
    print(
        dedent("""
    Select a task:
    1. Analyse string             | 16. Queue (two stacks)
    2. Remove multiple blanks     | 17. Singly-Linked list
    3. Reverse string             | 18. Doubly-linked list
    4. Toggle case                | 19. Binary Tree
    5. Compute word frequency
    6. Fibonacci (iterative)
    7. Fibonacci (recursive)
    9. Product (recursive)
    10. Division (recursive)
    11. Generate subsets
    12. Stack
    13. Evaluate postfix
    14. Queue
    15. Dequeue
    0. Exit
    """)
    )
    _option = input("Enter a number: ")
    match int(_option):
        case 0:
            return
        case 1:
            user_input = input("Enter a string: ")
            chars, blanks, words = analyse_string(user_input)
            print(
                f"Total characters: {chars},\nTotal blanks (spaces): {blanks},\nTotal words: {words}"
            )
        case 2:
            user_input = input("Enter a string: ")
            print(f"Result: {remove_multiple_blanks(user_input)}")
        case 3:
            user_input = input("Enter a string: ")
            print(reverse_string(user_input))
        case 4:
            user_input = input("Enter a string: ")
            print(toggle_case(user_input))
        case 5:
            user_input = input("Enter a string: ")
            words = compute_word_frequency_recursive(user_input)
            for i, c in words.items():
                print(f"'{i}': {c}")
        case 6:
            user_input = input("Enter a number: ")
            print(f"Fibonacci sequence for {user_input}: {fibonacci(int(user_input))}")
        case 7:
            user_input = input("Enter a number: ")
            print(f"Fibonacci sequence for {user_input}: {fibonacci_recursive(int(user_input))}")
        case 9:
            user_input = input("Enter 2 numbers separated by space: ")
            numbers = list(map(int, user_input.split()))
            print(
                f"Product of {numbers[0]} and {numbers[1]}: {product_recursive(numbers[0], numbers[1])}"
            )
        case 10:
            user_input = input("Enter 2 numbers separated by space: ")
            numbers = list(map(int, user_input.split()))
            print(
                f"Product of {numbers[0]} and {numbers[1]}: {division_recursive(numbers[0], numbers[1])}"
            )
        case 11:
            user_input = input("Enter elements separated by space: ").split()
            print(f"Result: {generate_subsets(user_input)}")
        case 12:
            st = Stack()
            stack(st)
        case 13:
            user_input = input("Enter an expression: ")
            print(f"Result: {evaluate_postfix(user_input.split())}")
        case 14:
            qu = Queue()
            iqueue(qu)
        case 15:
            qu = IDeque()
            ideque(qu)
        case 16:
            qu = Queue2()
            iqueue2(qu)
        case 17:
            ll = LinkedList()
            linked_list(ll)
        case 18:
            dll = DoublyLinkedList()
            doubly_linked_list(dll)
        case 19:
            bt = BinaryTree()
            binary_tree(bt)
        case _:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
