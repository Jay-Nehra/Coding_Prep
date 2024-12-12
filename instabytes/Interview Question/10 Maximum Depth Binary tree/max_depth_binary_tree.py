"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None


class BinaryTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, value, parent=None, position=None):
        if not self.root:
            self.root = Node(value)
            print(f"Inserted root node with value {value}.")
        else:
            if self._contains(self.root, value):
                print(f"Value {value} already exists in the tree.")
                return
            if parent is None:
                print("Parent must be specified when inserting nodes beyond the root.")
                return
            inserted = self._insert_recursive(self.root, value, parent, position)
            if not inserted:
                print(f"Failed to insert node {value} as {position} child of {parent}.")

    def _contains(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        return self._contains(node.left, value) or self._contains(node.right, value)

    def _insert_recursive(self, current_node, value, parent, position):
        if current_node.value == parent:
            if position == "left":
                if current_node.left is None:
                    current_node.left = Node(value)
                    print(f"Inserted node {value} as left child of {parent}.")
                    return True
                else:
                    print(f"Left child of node {parent} is already occupied.")
                    return False
            elif position == "right":
                if current_node.right is None:
                    current_node.right = Node(value)
                    print(f"Inserted node {value} as right child of {parent}.")
                    return True
                else:
                    print(f"Right child of node {parent} is already occupied.")
                    return False
            else:
                print("Position must be 'left' or 'right'.")
                return False

        # Traverse left subtree
        if current_node.left:
            if self._insert_recursive(current_node.left, value, parent, position):
                return True

        # Traverse right subtree
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

    def max_depth(self, node=None, visited=None):
        if visited is None:
            visited = set()
        if node is None:
            node = self.root
        if node is None:
            return 0
        if node.value in visited:
            print(f"Cycle detected at node {node.value}. Stopping recursion.")
            return 0
        print(f"Visiting node: {node.value}")
        visited.add(node.value)
        left_depth = self.max_depth(node.left, visited.copy())
        right_depth = self.max_depth(node.right, visited.copy())
        depth = 1 + max(left_depth, right_depth)
        return depth


def main():
    tree = BinaryTree()

    print("Binary Tree Interactive Tester")
    print("Commands:")
    print("  insert <value> <parent> <position> - Insert a node")
    print("    Example: insert 5 10 left (Insert value 5 as the left child of 10)")
    print("  show - Print the tree")
    print("  depth - Calculate the maximum depth of the tree")
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
        elif command == "depth":
            depth = tree.max_depth()
            print(f"Maximum depth of the tree: {depth}")
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
