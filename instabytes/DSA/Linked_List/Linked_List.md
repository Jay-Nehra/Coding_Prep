## Python Linked List

LL is similar to arrays in that it is a type of linear data structure. we can use the classes to implement the Linked List (LL) in Python. LL consists of nodes. Each node consists of two elements i.e. data and the reference to the next node in the LL. 

First node in the LL is called `Head` node of the list and this can be used to access all the elements of the LL. 

### Implementation

We can start by initializing the node with the `__init__` method with an empty head. Next, we can add methods to add the nodes to LL. We can start with few basic methods to insert the nodes in the LL to specific places in the LL like `in the beginning`, `in the end` or removing the node which takes the node value and removes that from the LL. and other methods for getting the size of the LL and travesing the LL and prints the complete LL. 


## Cycle Detection (Floyd's Tortoise and Hare Algorithm)
> Why: Detecting cycles in a linked list is crucial because cycles can lead to infinite loops in traversal and other operations. Floyd's algorithm efficiently detects cycles with O(n) time complexity and O(1) space complexity.

### Steps for Cycle Detection

- Initialize Two Pointers:
    - slow: Moves one step at a time.
    - fast: Moves two steps at a time.
- Traversal:
    - Move slow and fast until fast reaches the end (no cycle) or slow meets fast (cycle detected).
- Cycle Detection:
    - If slow equals fast, there is a cycle.
    - If fast reaches the end, there is no cycle.