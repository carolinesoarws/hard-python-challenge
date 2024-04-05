

# Fist example of Simple Linked list
class Node:
    # creating a node with data and the next values
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

    def removeValue(self, node_to_remove):
        current_nome = self.head





def main():
    """
    # Creating some nots
    print("criando nós")
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    print("Nó 1: ", node1.data, "-->", node1.next)
    print("Nó 2: ", node2.data, "-->", node2.next)
    print("Nó 3: ", node3.data, "-->", node3.next)

    # Ligando os nós em uma lista encadeada
    # Linking the nots to a linked list
    print("linkado os nos em uma lista encadeada")
    node1.next = node2
    node2.next = node3

    print("Nó 1: ", node1.data, "-->", node1.next)
    print("Nó 2: ", node2.data, "-->", node2.next)
    print("Nó 3: ", node3.data, "-->", node3.next)


    # Percorrendo e imprimindo a lista encadeada
    # printing the linked list
    current_node = node1
    while current_node:
        # printing current node data
        print(current_node.data)
        current_node = current_node.next

    """

    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.display()

    print(linked_list)


if __name__ == "__main__":
    main()
