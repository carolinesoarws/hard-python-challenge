"""
01: Verifing if a linked list is empty
"""


class Node:
    def __init__(self, data=None):
        self.data = data  # value of the node
        self.next_node = None  # setting value of the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Value of the head of the node

    def is_empty(self):
        return self.head is None


# Running exercises
if __name__ == "__main__":

    linked_list = LinkedList()
    print(linked_list.is_empty())  # True
    linked_list.head = Node(1)
    print(linked_list.is_empty())  # False

