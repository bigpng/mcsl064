from collections import deque


# Exercise 18
class Node:
    def __init__(self, data: object) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    @staticmethod
    def insert(root: Node | None, key: object) -> Node:
        if root is None:
            return Node(key)
        queue = deque([root])

        while queue:
            temp = queue.popleft()
            # If left child is empty, insert the new node here
            if temp.left is None:
                temp.left = Node(key)
                break
            else:
                queue.append(temp.left)

            if temp.right is None:  # Same for right
                temp.right = Node(key)
                break
            else:
                queue.append(temp.right)

        return root

    # Exercise 19
    @staticmethod
    def inorder(root: Node | None) -> None:
        if root is None:
            return
        BinaryTree.inorder(root.left)
        print(root.data, end=" ")
        BinaryTree.inorder(root.right)

    @staticmethod
    def preorder(root: Node | None) -> None:
        if root is None:
            return
        print(root.data, end=" ")
        BinaryTree.preorder(root.left)
        BinaryTree.preorder(root.right)

    @staticmethod
    def postorder(root: Node | None) -> None:
        if root is None:
            return
        BinaryTree.postorder(root.left)
        BinaryTree.postorder(root.right)
        print(root.data, end=" ")

    # Exercise 20
    @staticmethod
    def inorderTraversal(root: Node | None) -> None:
        stack: list[Node] = []  # Nodes visited but not printed yet
        current = root  # Node currently examining

        while current is not None or stack:
            while current is not None:  # Go as left as possible
                stack.append(current)  # stack.append(10)
                current = current.left  # current = 10.left

            current = stack.pop()
            print(current.data, end=" ")
            current = current.right

    @staticmethod
    def preorderTraversal(root: Node | None) -> None:
        if root is None:
            return
        stack = [root]

        while stack:
            current = stack.pop()
            print(current.data, end=" ")
            # Push right first so left is processed first.
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

    @staticmethod
    def postorderTraversal(root: Node | None) -> None:
        if root is None:
            return
        stack1 = [root]
        stack2: list[Node] = []

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left is not None:
                stack1.append(current.left)
            if current.right is not None:
                stack1.append(current.right)

        while stack2:
            print(stack2.pop().data, end=" ")


def binary_tree(bt: BinaryTree) -> None:
    while True:
        option = int(
            input(
                "Enter an operation: 1. Insert;  2. Traverse (In-order); 3. Traverse (Pre-order); 4. Traverse (Post-order); 5. Traverse (In-order - Non-Recursive);    6. Traverse (Pre-order - Non-Recursive); 7. Traverse (Post-order - Non-Recursive);  0. Exit: "
            )
        )
        match option:
            case 0:
                break
            case 1:
                user_input = int(input("Enter an element: "))
                bt.root = bt.insert(bt.root, user_input)
            case 2:
                bt.inorder(bt.root)
                print()
            case 3:
                bt.preorder(bt.root)
                print()
            case 4:
                bt.postorder(bt.root)
                print()
            case 5:
                bt.inorderTraversal(bt.root)
                print()
            case 6:
                bt.preorderTraversal(bt.root)
                print()
            case 7:
                bt.postorderTraversal(bt.root)
                print()
            case _:
                print("Invalid entry")


# Exercise 21
class BST:
    def __init__(self, data: int | None = None) -> None:
        self.data = data
        self.left: BST | None = None
        self.right: BST | None = None

    @staticmethod
    def insert(root: BST | None, data: int) -> BST:
        if root is None:
            return BST(data)
        if root.data is None:
            root.data = data
        elif data < root.data:
            root.left = BST.insert(root.left, data)
        elif data > root.data:
            root.right = BST.insert(root.right, data)

        return root

    @staticmethod
    def search(root: BST | None, data: int) -> BST | None:
        if root is None or root.data is None:
            return None
        if root.data == data:
            return root
        elif data < root.data:
            return BST.search(root.left, data)
        else:
            return BST.search(root.right, data)

    @staticmethod
    def _find_min(root: BST) -> BST:
        current = root
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def delete(root: BST | None, data: int) -> BST | None:
        if root is None or root.data is None:
            return None

        if data < root.data:
            root.left = BST.delete(root.left, data)
        elif data > root.data:
            root.right = BST.delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            successor = BST._find_min(root.right)
            if successor.data is not None:
                root.data = successor.data
                root.right = BST.delete(root.right, successor.data)
        return root

    @staticmethod
    def inorder(root: BST | None) -> None:
        if root is None:
            return
        BST.inorder(root.left)
        print(root.data, end=" ")
        BST.inorder(root.right)

    @staticmethod
    def preorder(root: BST | None) -> None:
        if root is None:
            return
        print(root.data, end=" ")
        BST.preorder(root.left)
        BST.preorder(root.right)

    @staticmethod
    def postorder(root: BST | None) -> None:
        if root is None:
            return
        BST.postorder(root.left)
        BST.postorder(root.right)
        print(root.data, end=" ")


def bst(root: BST) -> None:
    while True:
        option = int(
            input(
                "Enter an operation: 1. Insert;  2. Traverse (In-order); 3. Traverse (Pre-order); 4. Traverse (Post-order); 5. Delete;  0. Exit: "
            )
        )
        match option:
            case 0:
                break
            case 1:
                user_input = input("Enter integers: ")
                for i in user_input.split():
                    root = root.insert(root, int(i))
            case 2:
                BST.inorder(root)
                print()
            case 3:
                BST.preorder(root)
                print()
            case 4:
                BST.postorder(root)
                print()
            case 5:
                user_input = input("What to delete? ")
                root.delete(root, int(user_input))
                print()
            case _:
                print("Invalid entry")
