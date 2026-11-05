# Exercise 13
class Queue:
    def __init__(self) -> None:
        self.items: list[object] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0  # Check if stack empty

    def enqueue(self, item: object) -> None:
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self) -> object:
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.items.pop(0)

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.items[0]

    def size(self) -> int:
        return len(self.items)


def iqueue(qu: Queue) -> None:
    while True:
        option = int(
            input("Enter an operation: 1. Enqueue;  2. Dequeue; 3. Peek;  4. Size;  0. Exit: ")
        )
        match option:
            case 0:
                break
            case 1:
                num = input("Enter an element: ")
                qu.enqueue(num)
            case 2:
                print(qu.dequeue())
            case 3:
                print(qu.peek())
            case 4:
                print(qu.size())
            case _:
                print("Invalid entry")


# Exercise 14
class IDeque:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def add_front(self, item: object) -> None:
        self.items.insert(0, item)
        print(f"Added to front: {item}")

    def add_rear(self, item: object) -> None:
        self.items.append(item)
        print(f"Added to rear: {item}")

    def remove_front(self) -> object:
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop(0)

    def remove_rear(self) -> object:
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop()

    def peek_front(self) -> object:
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.items[0]

    def peek_rear(self) -> object:
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


def ideque(qu: IDeque) -> None:
    while True:
        option = int(
            input(
                "Enter an operation: 1. Add Front;  2. Add Rear; 3. Remove Front;  4. Remove Rear;  5. Peek Front;  6. Peek Rear; 7. Size;  0. Exit: "
            )
        )
        match option:
            case 0:
                break
            case 1:
                num = input("Enter an element: ")
                qu.add_front(num)
            case 2:
                num = input("Enter an element: ")
                qu.add_rear(num)
            case 3:
                print(qu.remove_front())
            case 4:
                print(qu.remove_rear())
            case 5:
                print(qu.peek_front())
            case 6:
                print(qu.peek_rear())
            case 7:
                print(qu.size())
            case _:
                print("Invalid entry")


# Exercise 15
class Queue2:
    def __init__(self) -> None:
        self.stack_in = []
        self.stack_out = []

    def is_empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def enqueue(self, item: object) -> None:
        self.stack_in.append(item)
        print(f"Enqueued: {item}")

    # transfer from stack_in to stack_out
    def _transfer(self) -> None:
        # Check whether stack_out is empty; only transfer when stack_out is empty
        if not self.stack_out:
            # As long as stack_in contains elements, keep transferring
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def dequeue(self) -> object:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        self._transfer()
        return self.stack_out.pop()

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("peek from empty queue")
        self._transfer()
        return self.stack_out[-1]

    def size(self) -> int:
        return len(self.stack_in) + len(self.stack_out)


def iqueue2(qu: Queue2) -> None:
    while True:
        option = int(
            input("Enter an operation: 1. Enqueue;  2. Dequeue; 3. Peek;  4. Size;  0. Exit: ")
        )
        match option:
            case 0:
                break
            case 1:
                num = input("Enter an element: ")
                qu.enqueue(num)
            case 2:
                print(qu.dequeue())
            case 3:
                print(qu.peek())
            case 4:
                print(qu.size())
            case _:
                print("Invalid entry")
