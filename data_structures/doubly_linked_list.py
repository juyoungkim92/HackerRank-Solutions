"""
Implementation of a doubly linked list

"""


class Node:
    """
    Node of a linked list.
    """
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """
    Doubly Linked list.
    """
    def __init__(self):
        """
        Constructor for empty doubly linked list.
        """
        self.head = None

    def insert_at_beginning(self, data):
        """
        Add node to the front of the list.
        """
        node = Node(data)
        node.next = self.head

        # if not an empty list i.e. there is one already
        if self.head is not None:
            self.head.prev = node

        # now the head is new node
        self.head = node

    def insert_at_the_end(self, data):
        """
        Append new node at the end
        """
        node = Node(data)
        node.next = None  # new node is at the last node so next is Null

        # if the linked list is empty
        if self.head is None:
            node.prev = None
            self.head = node
            return

        # if not, traverse till the end
        itr = self.head

        while itr.next is not None:
            itr = itr.next

        itr.next = node
        node.prev = itr

    @staticmethod
    def insert_after(prev_node, data):
        """
        Insert a new node after given prev node
        """
        if prev_node is None:
            raise Exception("The given previous node cannot be NULL")

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        # change new node's next's previous node is the new node.
        if new_node.next is not None:
            new_node.next.prev = new_node

    @staticmethod
    def print_linked_list(node):
        """
        Prints the linked list from a given point
        """
        print("Traverse in forward direction")
        linked_list = ""
        while node is not None:
            linked_list += str(node.data) + " <--> "
            last = node
            node = node.next
        print(linked_list)

        print("Traverse in reverse direction")
        linked_list = ""
        while last is not None:
            linked_list += str(last.data) + " <--> "
            last = last.prev
        print(linked_list)


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_the_end(1)  # insert 6 so it becomes 6->None
    dll.insert_at_beginning(2)  # insert 7 at the beginning so it becomes 7->6->None
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(4)
    print("Doubly linked list before insertion of 8")
    dll.print_linked_list(dll.head)

    # insert 8 after 5:
    # 3->5->8->7->6
    print("Doubly linked list after insertion of 8")
    dll.insert_after(dll.head.next.next, 8)
    dll.print_linked_list(dll.head)

# Doubly linked list before insertion of 8
# Traverse in forward direction
# 4 <--> 3 <--> 2 <--> 1 <-->
# Traverse in reverse direction
# 1 <--> 2 <--> 3 <--> 4 <-->

# Doubly linked list after insertion of 8
# Traverse in forward direction
# 4 <--> 3 <--> 2 <--> 8 <--> 1 <-->
# Traverse in reverse direction
# 1 <--> 8 <--> 2 <--> 3 <--> 4 <-->
