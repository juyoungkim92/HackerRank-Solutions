"""
Python implementation of Hash tables.

Dictionary is Python specific implementation of hash table.

# Hash function - converts the input (key) into an index to an array.
One way of hash function. Convert they key into ASCII and get a sum
and do a modulus with the size of array. For example 'march 6' -> 609 % 10 -> 9 (index)

Bad hash function results in Hash collision. Ways to resolve collision:
- Separate chaining
- Linear probing

"""


class HashTable:
    """
    Implementation of dictionary, hash table
    """
    def __init__(self):
        self.MAX = 100
        # self.arr = [None for _ in range(self.MAX)]

        # we now store empty list because we now storing Key-Value pair
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            # go through each character in key and find ASCII value and get a sum
            h += ord(char)

        return h % self.MAX  # doing a modulus, we assume 100 as size of list

    def __setitem__(self, key, value):  # def add() can be redefined as setitem
        """
        This allows for t['march 6'] = 130
        """
        h = self.get_hash(key)
        # self.arr[h] = value | previously this overrides the value

        # To resolve collision, we implement a separate chaining as linked list.
        # need to iterate linked list and find the right location
        # below is to handle if the key already existed.
        found = False
        for ind, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                # insert new tuple at the same location
                self.arr[h][ind] = (key, value)
                found = True
                break

        # if not found the key in the hash table
        # the below step creates a linked list
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):  # def get() can be redefined as __getitem__
        """
        This allows for t['march 6'] i.e. get
        """
        h = self.get_hash(key)

        # we modify get function to get items from a linked list such as [('march 6', 78), ('march 17' ,459)]
        # we look through the linked list (separate chain) and grab the correct key value
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        """
        This allows for del t['march 6']
        """
        h = self.get_hash(key)

        # below is to delete items in a linked list in a separate chained hash map (for avoiding collision)
        for ind, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][ind]


if __name__ == '__main__':
    t = HashTable()
    # t['march 6'] = 130
    # t['march 1'] = 20
    # print(t['march 6'])
    #
    # # delete
    # del t['march 6']

    # Resolving collision:
    # Below generates index of of
    # t.get_hash("march 6")
    # t.get_hash("march 17")
    #
    # t["march 6"] = 120
    # t["march 17"] = 459
    # t["march 6"] throws 459 because march 17 overrides the march 6 previously.

    print(t.get_hash("march 6"))
    print(t.get_hash("march 17"))

    t['march 6'] = 120  # index 9
    t['march 6'] = 78
    t['march 17'] = 459  # index 9 thus should create a linked list according to above logic
    print(t.arr)

    # delete items?
    del t['march 17']
