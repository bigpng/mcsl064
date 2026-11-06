# Exercise 16
class Node:
    def __init__(self, data: object) -> None:
        self.data = data
        self.next: Node | None = None  # stores a reference to next node
        self.prev: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def insert_at_beginning(self, data: object) -> None:
        new_node = Node(data)
        new_node.next = self.head  # Inserting at the beginning changes the head of the linked list
        self.head = new_node

    def insert_after_node(self, node: Node | None, data: object) -> None:
        if node is None:
            return

        new_node = Node(data)
        new_node.next = node.next  # Connect the new node to next node
        node.next = new_node  # Connect the original node to the new node

    def insert_at_end(self, data: object) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head  # Current is used to move through the linked list without changing head

        # Keep moving the next node as long as a next node exists
        # Stops when current.next is None
        while current.next:
            current = current.next

        current.next = new_node
        # As this is a pointer, it inserts at end

    def delete_at_beginning(self) -> None:
        if self.head is None:
            return

        self.head = self.head.next

    def delete_after_node(self, node: Node | None) -> None:
        if node is None or node.next is None:
            return

        # 10.next = 30: Change reference directly
        node.next = node.next.next

    def delete_at_end(self) -> None:
        if self.head is None or self.head.next is None:
            self.head = None
            return

        current = self.head

        # Stop at the second-last node
        while current.next is not None and current.next.next is not None:
            current = current.next

        current.next = None  # Disconnect the last node from current

    def find_node(self, param: object) -> Node | None:
        current = self.head
        while current is not None and current.data != param:
            current = current.next

        return current

    def traverse(self) -> None:
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


def linked_list(ll: LinkedList) -> None:
    while True:
        option = int(
            input(
                "Enter an operation: 1. Insert at beginning;  2. Insert after node; 3. Insert at end;  4. Delete from begining;  5. Delete after node; 6. Delete at end; 7. Traverse;  0. Exit: "
            )
        )
        match option:
            case 0:
                break
            case 1:
                user_input = int(input("Enter an element: "))
                ll.insert_at_beginning(user_input)
            case 2:
                user_input = int(input("Enter an element: "))
                after = int(input("Enter after: "))
                node = ll.find_node(after)
                ll.insert_after_node(node, user_input)
            case 3:
                user_input = int(input("Enter an element: "))
                ll.insert_at_end(user_input)
            case 4:
                ll.delete_at_beginning()
            case 5:
                user_input = int(input("Delete after: "))
                ll.delete_after_node(ll.find_node(user_input))
            case 6:
                ll.delete_at_end()
            case 7:
                ll.traverse()
            case _:
                print("Invalid entry")


# Exercise 17
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def insert_at_beginning(self, data: object) -> None:
        new_node = Node(data)
        # Note: Push down
        new_node.next = self.head  # Connect the new node to the existing head
        if self.head:  # Connect old head backwards to the new node
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data: object) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:  # Find the last node
            current = current.next

        current.next = new_node  # Connect new node (forward connection)
        new_node.prev = current  # Connect the new node backwards to the old last node

    def delete_at_beginning(self) -> None:
        if self.head is None:
            print("Doubly linked list is empty")
            return

        if self.head.next is None:  # Check whether there is only one node
            self.head = None
            return

        new_head = self.head.next  # Get the 2nd node from top
        new_head.prev = None  # New head has no previous node
        del self.head
        self.head = new_head

    def delete_at_end(self) -> None:
        if self.head is None:
            print("Doubly linked list is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next is not None and current.next.next is not None:
            current = current.next  # Find last node

        del_node = current.next
        current.next = None
        del del_node

    def traverse(self) -> None:
        # Traverse the doubly linked list and print its elements
        current = self.head
        while current:
            # Print current node's data
            print(current.data, end=" <-> ")
            # Move to the next node
            current = current.next
        print("None")


def doubly_linked_list(dll: DoublyLinkedList) -> None:
    while True:
        option = int(
            input(
                "Enter an operation: 1. Insert at beginning;  2. Insert at end;  3. Delete from begining;  4. Delete at end; 5. Traverse;  0. Exit: "
            )
        )
        match option:
            case 0:
                break
            case 1:
                user_input = int(input("Enter an element: "))
                dll.insert_at_beginning(user_input)
            case 2:
                user_input = int(input("Enter an element: "))
                dll.insert_at_end(user_input)
            case 3:
                dll.delete_at_beginning()
            case 4:
                dll.delete_at_end()
            case 5:
                dll.traverse()
            case _:
                print("Invalid entry")
