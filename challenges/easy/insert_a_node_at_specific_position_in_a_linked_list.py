"""

https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

Create a new node with the given integer and its data attribute, insert this node at the desired position
in a linked list and return the head node.

Given the pointer to the head node of a linked list, complete a function that returns a reference to the head node of the finished list.

Example:

linked list 16 -> 13 -> 7

insert value of 1 at position 2

new list:

16 -> 13 -> 1 -> 7

SinglyLinkedList is a Node class
such as

class SinglyLinkedList:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
"""


class SinglyLinkedList:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def insert_node_at_position(head, data, position):
    """
    :param head: head node of a linked list
    :param data: data to insert
    :param position: given index
    :return: reference to the head node i.e. HackerRank prints a new linked list

    Function explanation:

    1. if position is < 0 we throw error

    2. if position is at 0. This means the new head of linked list is the new Node therefore return the new node

    3. if position is 0 < p < nth number:

        In a linked list, we want to insert the new data -1 from the desired position.
        i.e. 16 [0] -> 7 [1] -> 3 [2], here if we want to insert at position 2, we need to modify the link such that
        value 7's pointer to the next element should be the new node.

        Thus, we set count = 0 and iterator the head and see if the count == position - 1.
        If count == position - 1 then we create a new Node and the new Node's next pointer is
        the next pointer from position - 1. The position - 1 Node's next pointer is the new Node.
        Therefore set itr.next = node <- New Node and break the loop

        The reference to the head will return the full linked list with modified pointers.

    """

    if position < 0:
        raise Exception(f"{position} is not a valid position.")

    if position == 0:
        node = SinglyLinkedList(data)

        # return new node which is the head node
        return node

    count = 0
    itr = head

    while itr:
        if count == position - 1:
            node = SinglyLinkedList(data)
            node.next = itr.next
            itr.next = node
            break

        itr = itr.next
        count += 1

    return head
