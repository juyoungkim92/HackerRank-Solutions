"""

Example of queue implementation in Python.

Queue is FIFO - First In First Out.

"""

from collections import deque

stock_price_queue = []
stock_price_queue.insert(0, 131.10)
stock_price_queue.insert(0, 132.13)
stock_price_queue.insert(0, 135)

# print the list
# [135, 131.13, 131.10]
stock_price_queue.pop()  # 131.1 FIFO
stock_price_queue.pop()  # 132.13
stock_price_queue.pop()  # 135
stock_price_queue.pop()  # exception pop from empty list.

# While list can work okay, it has problems with dynamic arrays
# allocate new element and if exceeds the capacity, will have to allocate new memory area and copy
# list is not recommended.

# Using DQ from collections module
# can be used as a stack or queue
# stack -> append
# queue -> append left

q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(1)
q.pop()  # 5 comes out first
q.pop()  # 8 comes out second


# Proper queue class using collections deque

class Queue:
    """
    Queue class.
    """
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(
        {
            "company": "Apple",
            "timestamp": "15 Oct, 11:01 AM",
            "price": 131.10
        })

    q.enqueue(
        {
            "company": "Apple",
            "timestamp": "15 Oct, 13:01 PM",
            "price": 130.10
        })

    q.enqueue(
        {
            "company": "Apple",
            "timestamp": "15 Oct, 15:01 PM",
            "price": 128.10
        })

    # q.buffer  # shows elements
    q.dequeue()  # get the first element
    q.dequeue()  # get the second element
    q.dequeue()  # get the third element

    # if you dequeue() i.e. pop() more than the values inside, you'll get an exception
    # IndexError: pop from an empty deque
    q.size()
    q.is_empty()
