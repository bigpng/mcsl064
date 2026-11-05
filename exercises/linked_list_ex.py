# Exercise 16
class Node:
    def __init__(self, data: object) -> None:
        self.data = data
        self.next: Node | None = None  # stores a reference to next node
        self.prev: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    @staticmethod
    def insert_at_beginning(head: Node | None, data: object) -> Node:
        new_node = Node(data)
        new_node.next = head  # Inserting at the beginning changes the head of the linked list
        return new_node

    @staticmethod
    def insert_after_node(node: Node | None, data: object) -> None:
        if node is None:
            return

        new_node = Node(data)
        new_node.next = node.next  # Connect the new node to next node
        node.next = new_node  # Connect the original node to the new node

    @staticmethod
    def insert_at_end(head: Node | None, data: object) -> Node:
        new_node = Node(data)
        if head is None:
            return new_node

        current = head  # Current is used to move through the linked list without changing head

        # Keep moving the next node as long as a next node exists
        # Stops when current.next is None
        while current.next:
            current = current.next

        current.next = new_node
        return head

    @staticmethod
    def delete_at_beginning(head: Node | None) -> Node | None:
        if head is None:
            return None

        return head.next

    @staticmethod
    def delete_after_node(node: Node | None) -> None:
        if node is None or node.next is None:
            return

        # 10.next = 30: Change reference directly
        node.next = node.next.next

    @staticmethod
    def delete_at_end(head: Node | None) -> Node | None:
        if head is None or head.next is None:
            return None

        current = head

        # Stop at the second-last node
        while current.next is not None and current.next.next is not None:
            current = current.next

        current.next = None  # Disconnect the last node from current
        return head

    @staticmethod
    def find_node(head: Node | None, param: object) -> Node | None:
        current = head
        while current is not None and current.data != param:
            current = current.next

        return current

    @staticmethod
    def traverse(head: Node | None) -> None:
        current = head

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
                ll.head = ll.insert_at_beginning(ll.head, user_input)
            case 2:
                user_input = int(input("Enter an element: "))
                after = int(input("Enter after: "))
                node = ll.find_node(ll.head, after)
                ll.insert_after_node(node, user_input)
            case 3:
                user_input = int(input("Enter an element: "))
                ll.head = ll.insert_at_end(ll.head, user_input)
            case 4:
                ll.head = ll.delete_at_beginning(ll.head)
            case 5:
                user_input = int(input("Delete after: "))
                ll.delete_after_node(ll.find_node(ll.head, user_input))
            case 6:
                ll.head = ll.delete_at_end(ll.head)
            case 7:
                ll.traverse(ll.head)
            case _:
                print("Invalid entry")


# Exercise 17
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    @staticmethod
    def insert_at_beginning(head: Node | None, data: object) -> Node:
        new_node = Node(data)
        # Note: Push down
        new_node.next = head  # Connect the new node to the existing head
        if head:  # Connect old head backwards to the new node
            head.prev = new_node
        return new_node

    @staticmethod
    def insert_at_end(head: Node | None, data: object) -> Node:
        new_node = Node(data)
        if head is None:
            return new_node

        current = head
        while current.next:  # Find the last node
            current = current.next

        current.next = new_node  # Connect new node (forward connection)
        new_node.prev = current  # Connect the new node backwards to the old last node
        return head

    @staticmethod
    def delete_at_beginning(head: Node | None) -> Node | None:
        if head is None:
            print("Doubly linked list is empty")
            return None

        if head.next is None:  # Check whether there is only one node
            return None

        new_head = head.next  # Get the 2nd node from top
        new_head.prev = None  # New head has no previous node
        del head
        return new_head

    @staticmethod
    def delete_at_end(head: Node | None) -> Node | None:
        if head is None:
            print("Doubly linked list is empty")
            return None

        if head.next is None:
            return None

        current = head
        while current.next is not None and current.next.next is not None:
            current = current.next  # Find last node

        del_node = current.next
        current.next = None
        del del_node
        return head

    @staticmethod
    def traverse(head: Node | None) -> None:
        # Traverse the doubly linked list and print its elements
        current = head
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
                dll.head = dll.insert_at_beginning(dll.head, user_input)
            case 2:
                user_input = int(input("Enter an element: "))
                dll.head = dll.insert_at_end(dll.head, user_input)
            case 3:
                dll.head = dll.delete_at_beginning(dll.head)
            case 4:
                dll.head = dll.delete_at_end(dll.head)
            case 5:
                dll.traverse(dll.head)
            case _:
                print("Invalid entry")
