"""
Python implementation of Hash tables.

Dictionary is Python specific implementation of hash table.

"""


class HashTable:
    """
    Implementation of dictionary, hash table
    """
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

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
        self.arr[h] = value

    def __getitem__(self, item):  # def get() can be redefined as __getitem__
        """
        This allows for t['march 6'] i.e. get
        """
        h = self.get_hash(item)

        return self.arr[h]

    def __delitem__(self, key):
        """
        This allows for del t['march 6']
        """
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 130
    t['march 1'] = 20
    print(t['march 6'])

    # delete
    del t['march 6']
