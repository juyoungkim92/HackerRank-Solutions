"""
Python example of implementation of Stack using two queues.

Algorithm:

Queue --> FIFO (first in first out)
Stack --> LIFO (last in first out)

This is pop() costly operation.

0. Initialise two queues q1 and q2
1. We insert value into q1
2. We move everything from q1 to q2 except the last element from q1
3. Store the last element from q1 to temp and pop()
4. We switch q2 and q1 such that now q2 is empty.
5. Do the same again.


push 1,2,3 and move everything until n = 1
    ------------
q1     3
    ------------

    ------------
q2     1 2
    ------------

temp = 3

q1 is empty

q2 has 1, 2

switch q1 and q2

"""

from collections import deque


class Stack:
    """ class stack. """
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, data):
        # push item to the first queue
        self.q1.append(data)

    def pop(self):
        # check if q1 is empty
        if not self.q1:
            raise Exception("The queue is empty")

        # move all elements from q1 to q2 except last element
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        deque_val = self.q1.popleft()

        # switch q1 and q2 i.e. move all elements from q2 back to q1
        while self.q2:
            self.q1.append(self.q2.popleft())

        return deque_val


if __name__ == '__main__':
    # here our stack should return 3 as first element according to LIFO
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Current queue1: {s.q1}")
    print(f"Current queue2: {s.q2}")

    # dequeue
    print(f"1st popped value from stack: {s.pop()}")
    print(f"2nd popped value from stack: {s.pop()}")
    print(f"3rd popped value from stack: {s.pop()}")  # 3 returned

    # after 3rd queue, it will throw error
    print(f"4th popped value from stack: {s.pop()}")
