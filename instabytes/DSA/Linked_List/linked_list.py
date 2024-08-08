from loguru import logger
from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
    
    def insert_at_beginning(self, value: int) -> None:
        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node
        logger.info(f"Inserted {value} at the beginning of the list.")

    def insert_at_index(self, value: int, index: int) -> None:
        if index == 0:
            self.insert_at_beginning(value)
            return
        
        current = self.head
        for i in range(index - 1):
            if current is None:
                logger.error(f"Index `{index}` is not present in the LL.")
                return
            current = current.next
        
        if current is not None:
            new_node = Node(value=value)
            new_node.next = current.next
            current.next = new_node
            logger.info(f"Inserted the value {value} at the index {index}.")
        else:
            logger.error(f"Index `{index}` is not present in the LL.")

    def insert_at_end(self, value: int) -> None:
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            logger.info(f"Inserted {value} at the end of the list (was empty).")
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
        logger.info(f"Inserted {value} at the end of the list.")

    def update_node(self, value: int, index: int) -> None:
        current = self.head
        position = 0 
        
        while current is not None and position != index:
            position += 1
            current = current.next
        
        if current is not None:
            current.value = value
            logger.info(f"Updated the node at index {index} to value {value}.")
        else:
            logger.error(f"Index `{index}` is not present in the LL.")

    def remove_first_node(self) -> None:
        if self.head is None:
            logger.warning("Tried to remove first node, but list is empty.")
            return
        
        self.head = self.head.next
        logger.info("Removed the first node from the list.")
        
    def remove_last_element(self) -> None:
        if self.head is None:
            logger.warning("Tried to remove last node, but list is empty.")
            return
        
        if self.head.next is None:
            self.head = None
            logger.info("Removed the last node from the list (was the only node).")
            return
        
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        current.next = None
        logger.info("Removed the last node from the list.")

    def remove_at_index(self, index: int) -> None:
        if self.head is None:
            logger.warning("Tried to remove node at index, but list is empty.")
            return
        
        current = self.head
        position = 0 
        
        if position == index:
            self.remove_first_node()
            logger.info(f"Removed node at index {index} (first node).")
            return
        
        while current.next is not None and position != index - 1:
            position += 1
            current = current.next
            
        if current.next is not None:
            current.next = current.next.next
            logger.info(f"Removed node at index {index}.")
        else:
            logger.error(f"Index `{index}` is not present in the LL.")

    def remove_node(self, value: int) -> None:
        current = self.head
        previous = None
        
        if current is None:
            logger.error("Cannot remove from an empty list.")
            return
        
        if current.value == value:
            self.remove_first_node()
            logger.info(f"Removed node with value `{value}` (head of the list).")
            return
        
        while current is not None and current.value != value:
            previous = current
            current = current.next
        
        if current is None:
            logger.error(f"Value `{value}` is not present in the LL.")
            return
        
        if previous is not None:
            previous.next = current.next
            logger.info(f"Removed node with value `{value}`.")
    
    def traverse_ll(self) -> None:
        current = self.head
        while current:
            logger.info(current.value)
            current = current.next

    def ll_size(self) -> int:
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        logger.info(f"Linked list size is {size}.")
        return size
