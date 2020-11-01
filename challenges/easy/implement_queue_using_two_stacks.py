"""
Implementing Queue using Two stacks.

Queue --> FIFO (first in first out)
Stack --> LIFO (last in first out)

Implementation:

1. There are two operations enqueue and dequeue. The caller doesn't know about stacks underneath (abstracted)
2. enqueue, insert the value to the stack1
3. in dequeue, if stack2 is empty, move everything from stack1 to stack2
4. still in dequeue, pop the element from stack2

    stack1                                 stack2
    | 5 | last item entered                | 1 | last item entered (goes out first)
    | 4 |                                  | 2 |                                     Queue
    | 3 |                      --->        | 3 |                                    -------->  | 1 2 3 4 5 |
    | 2 |                                  | 4 |
    | 1 | first item entered               | 5 | first item entered

"""


class Queue:
    def __init__(self):
        """
        Initialise stacks
        """
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        """
        function to insert value into stack1
        """
        self.s1.append(data)

    def dequeue(self):
        """
        function to dequeue from stack2
        """
        if len(self.s1) == 0 and len(self.s2) == 0:
            raise Exception("The Queue is empty.")

        # if s2 is empty and s1 has elements, move elements from s1 to s2
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp_var = self.s1.pop()  # pop default index is -1
                self.s2.append(temp_var)

            # finally once everything moved, pop from stack2
            return self.s2.pop()

        # if s2 is not empty, just pop from s2
        else:
            return self.s2.pop()


if __name__ == '__main__':
    # When enqueue 1,2,3 sequentially, dequeue must return 1,2,3
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)  # [1, 2, 3]
    print(f"stack 1: {q.s1}")

    print(q.dequeue())  # returns 1
    print(f"stack 2 after 1st dequeue: {q.s2}")
    print(q.dequeue())  # returns 2
    print(f"stack 2 after 2nd dequeue: {q.s2}")
    print(q.dequeue())  # returns 3
    print(f"stack 2 after 3rd dequeue: {q.s2}")
