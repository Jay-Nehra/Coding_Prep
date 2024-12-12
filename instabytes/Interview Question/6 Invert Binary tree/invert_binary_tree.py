"""
LC-226 Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from loguru import logger
from dataclasses import dataclass


@dataclass
class Node:
    """
    Node dataclass.
    """

    value: int
    left: "Node" = None
    right: "Node" = None


class BinaryTree:
    def __init__(self):
        self.root: Node = None

    def _contains(self, node: Node, value: int) -> bool:
        """
        It is used to check if the value already exists in the tree.
        """
        if node is None:
            return False
        if node.value == value:
            return True

        return self._contains(node.left, value) or self._contains(node.right, value)

    def insert(self, value: int, parent=None, position=None):
        if self.root is None:
            self.root = Node(value)
            return

        else:
            if self._contains(self.root, value):
                logger.info(f"A node with value {value} already exists in the tree.")
                return
            if parent is None:
                logger.info(
                    "Parent must be specified when inserting nodes beyond the root."
                )
                return
            inserted = self._insert_recursive(self.root, value, parent, position)
            if not inserted:
                logger.error(
                    f"Failed to insert node {value} as {position} child of {parent}."
                )

    def _insert_recursive(self, current_node, value, parent, position):
        """
        Recursively traverse the tree to find the parent node, then insert the new value
        into the available child node (left or right) based on its availability.
        """
        if current_node.value == parent:
            if position == "left":
                if current_node.left is None:
                    current_node.left = Node(value)
                    logger.info(f"Inserted node {value} as left child of {parent}.")
                    return True
                else:
                    logger.info(f"Left child of node {parent} is already occupied.")
                    return False
            elif position == "right":
                if current_node.right is None:
                    current_node.right = Node(value)
                    logger.info(f"Inserted node {value} as right child of {parent}.")
                    return True
                else:
                    logger.info(f"Right child of node {parent} is already occupied.")
                    return False
            else:
                logger.info("Position must be 'left' or 'right'.")
                return False

        if current_node.left:
            if self._insert_recursive(current_node.left, value, parent, position):
                return True

        if current_node.right:
            if self._insert_recursive(current_node.right, value, parent, position):
                return True

        return False

    def __repr__(self):
        if not self.root:
            return "Binary Tree is empty."
        return self._repr_recursive(self.root)

    def _repr_recursive(self, node, level=0):
        if not node:
            return ""
        result = ""
        result += self._repr_recursive(node.right, level + 1)
        result += f"{' ' * (4 * level)}{node.value}\n"
        result += self._repr_recursive(node.left, level + 1)
        return result

    def invert(self, node: Node = None):
        if node is None:
            node = self.root
        if node is None:
            logger.error(
                "The tree is empty. Please populate the tree before inverting."
            )
            return
        return self._invert_recursive(node)

    def _invert_recursive(self, node: Node):
        if node is None:
            return

        node.left, node.right = node.right, node.left
        self._invert_recursive(node.left)
        self._invert_recursive(node.right)


def main():
    tree = BinaryTree()

    print("Binary Tree Interactive Tester")
    print("Commands:")
    print("  insert <value> <parent> <position> - Insert a node")
    print("    Example: insert 5 10 left (Insert value 5 as the left child of 10)")
    print("  show - Print the tree")
    print("  invert - Invert the tree")
    print("  quit - Exit the program")

    while True:
        command = input("\nEnter a command: ").strip().lower()

        if command == "quit":
            print("Exiting...")
            break
        elif command == "show":
            print(tree)
        elif command.startswith("insert"):
            parts = command.split()
            if len(parts) == 2:  # Insert root
                value = int(parts[1])
                tree.insert(value)
            elif len(parts) == 4:
                value, parent, position = int(parts[1]), int(parts[2]), parts[3].lower()
                if position not in {"left", "right"}:
                    print("Invalid position. Use 'left' or 'right'.")
                    continue
                tree.insert(value, parent, position)
            else:
                print("Invalid insert command. Use: insert <value> <parent> <position>")
        elif command == "invert":
            tree.invert()
            print(tree)
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
