"""
Python implementation of a Linked list.

"""


class Node:
    """
    Usual element in a Linked List.
    """
    def __init__(self, data=None, next=None):
        """
        :param data: the value
        :param next: pointer to the next element.
        """
        self.data = data
        self.next = next


class LinkedList:
    """ Linked List class. """
    def __init__(self):
        self.head = None  # head variable refers to the head of Linked List

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        iterator = self.head
        linked_list = ""

        while iterator:
            linked_list += str(iterator.data) + " --> "
            iterator = iterator.next

        print(linked_list)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head  # self.head = Node(data, Node(data, None)) if 2 inserted

        while iterator.next:

            # 1st cycle: Node(data, None)
            # 2nd cycle: Node(data, Node(data, None)) ... and so on

            iterator = iterator.next

        iterator.next = Node(data, None)

    def insert_values(self, data_list):
        """
        Method to insert list of values as input and create a new fresh linked list
        """
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """
        Method to count length of a linked list
        """
        count = 0
        iterator = self.head

        while iterator:
            count += 1
            iterator = iterator.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")

        # if want to remove value at index 0? Which is a head
        if index == 0:
            self.head = self.head.next
            return

        count = 0  # in linked list you have to manually maintain the count to reach the particular index
        iterator = self.head

        # go through the linked list
        # in linked list you want to stop at an element prior to the element you want to remove
        # in that element you can modify the link and the link is the next length that you have
        while iterator:
            if count == index - 1:
                iterator.next = iterator.next.next
                break

            iterator = iterator.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        iterator = self.head

        while iterator:
            if count == index - 1:
                node = Node(data, iterator.next)
                iterator.next = node
                break

            iterator = iterator.next
            count += 1


if __name__ == '__main__':
    linked_list = LinkedList()

    # Part A.
    # linked_list.insert_at_beginning(5)  # insert 5 first
    # linked_list.insert_at_beginning(89)  # insert 89 next and 5 shifts so 89 --> 5
    # linked_list.insert_at_end(79)

    # Part B.
    linked_list.insert_values(["test1", "test2", "test3", "test4"])

    # Part C.
    # print("LinkedList length:", linked_list.get_length())

    # Part D.
    # linked_list.remove_at(2)

    # Part E.
    linked_list.insert_at(0, "figs")
    linked_list.insert_at(2, "mango")
    linked_list.insert_at(5, 55)
    linked_list.insert_at(6, "banana")
    linked_list.remove_at(1)

    # Print Linked List
    linked_list.print_linked_list()
