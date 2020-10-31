"""

This question is not from HackerRank but is a frequently asked question.

Given pointer to the head node of a linked list, the task is to reverse the linked list.

For example:

1 -> 2 -> 3 -> 4 -> Null
4 -> 3 -> 2-> 1 -> Null

"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        """
        Initialize head node
        """
        self.head = None

    def insert_at_beginning(self, data):
        """
        Function to insert a new node at the beginning
        """
        node = Node(data, self.head)
        self.head = node

    def reverse_linked_list(self):
        """
        Function to reverse a given linked list.

        Explain how while loop works:

        A -> B -> C -> D
        D -> C -> B -> A
        A <- B <- C <- D

        We want to modify the pointer such that the Node's next is previous
        We first set temporary 'next' variable which is the current node's next node
        We than set current node's next to previous node (modifying link)
        We than set previous node for the next node such that 'prev = current node'
        We than also set the new current node to next node such that 'current_node = next'
        """

        prev = None
        cur_node = self.head

        while cur_node:
            next = cur_node.next  # temporary variable pointing to the next
            cur_node.next = prev  # set current node's next to previous one
            prev = cur_node
            cur_node = next

        # set head of the node to the last node
        # in the while loop we set current node as prev so self.head = prev will work.
        self.head = prev

    def print_linked_list(self):
        """
        Function to print the linked list.
        """
        if self.head is None:
            raise Exception("Linked list is empty.")

        itr = self.head
        linked_list = ""

        while itr:
            linked_list += str(itr.data) + " --> "
            itr = itr.next

        print(linked_list)


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_beginning(56)
    llist.insert_at_beginning(20)
    llist.insert_at_beginning(37)
    llist.insert_at_beginning(11)
    print("Given Linked List")
    llist.print_linked_list()

    print("Reversed Linked List")
    llist.reverse_linked_list()
    llist.print_linked_list()
