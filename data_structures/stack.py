"""
Implement browser history back functionality using stack.

"""

from collections import deque

s = []

s.append("https://www.cnn.com")
s.append("https://www.cnn.com/world")
s.append("https://www.cnn.com/india")
s.append("https://www.cnn.com/china")

# get last from append and remove
s.pop()  # https://www.cnn.com/china
s.pop()  # https://www.cnn.com/india

# if you don't want to remove element
# s[-1]

# You can use list as a stack but in Python it is a dynamic array
# When there is extra capacity needed in the memory, it will copy the original to the new capacity
# thus it has to allocate new memory but it needs to copy all existing elements.
# This is problem because if there are millions elements, it is costly.
# thus using list as a stack is not recommended.

# collections.deque is used
# it uses, doubly linked list, don't need to preallocate memory (array has to preallocate). It allocates memory when needed
# no need to worry about copying elements to a new memory.

# implement stack using deque
stack = deque()
stack.append("https://www.cnn.com")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")

stack.pop()  # returns last and removes the last element


class Stack:
    """
    stack class using deque. Just to follow proper stack prototype.
    """
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_emtpy(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.peek()  # return 5 but will not remove 5 from the stack
    s.pop()  # return 5 and remove 5 from the stack
    s.is_emtpy()  # True because 5 was removed

    s.push(65)
    s.push(5)
    s.push(76)
    s.size()  # 3
