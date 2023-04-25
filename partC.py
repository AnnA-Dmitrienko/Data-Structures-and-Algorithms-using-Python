# Assignment-#2
# Student name: Anna Dmitrienko
# Student ID - 120-412-218
# Email - admitrienko@myseneca.ca


class ChainingTable:

    # packaging the key-value pair into one object
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, cap=32):
        # this initializes a list of capacity length with None and size 0
        self.the_table = [None]*cap  # also: [None for i in range(self.cap)]
        self.cap = cap
        self.size = 0

# adds a new key-value pair to the table
# if a record with same key exists, do not add - return false
# if doesn't - return True and insert then check load factor
# adjust capacity if load factor is >1.0
    def insert(self, key, value):
        hash_value = hash(key)
        idx = hash_value % self.cap
        node = self.the_table[idx]
        # traverse the nodes and see if such key exists
        while (node):
            if (node.key == key):
                print(f'key {node.key} already exists in the table')
                return False  # THE KEY IS ALREADY IN THE TABLE
            node = node.next  # keep going

        # create a new node at the same index and chain them together
        new_node = self.Record(key, value)
        new_node.next = self.the_table[idx]
        self.the_table[idx] = new_node
        self.size += 1  # adjust the size
        # check and adjust load factor
        load_factor = self.size/self.cap
        if (load_factor > 1.0):
            print("load factor is larger than 1, adjusting table capacity")
            new_table = [None for i in range(self.cap*2)]
            for i in range(self.cap):
                new_table[i] = self.the_table[i]
            self.the_table = new_table
            self.cap *= 2
        print(
            f'new node with key {new_node.key} and value {new_node.value} has been inserted')
        return True

    # modifies an existing key-value pair in the table. If no record
    # with matching key exists ->return False else returns True

    def modify(self, key, value):
        hash_value = hash(key)
        idx = hash_value % self.cap
        node = self.the_table[idx]
        while (node):
            if (node.key == key):
                print(f'value {node.value} has been modified')
                node.value = value
                return True
            node = node.next
        return False

    # removes a record and returns True, else return False
    def remove(self, key):
        hash_value = hash(key)
        idx = hash_value % self.cap
        node = self.the_table[idx]
        previous = None
        while (node):
            if (node.key == key):
                if (previous):  # if this wasn't the first node
                    previous.next = node.next  # connect prev with next
                else:  # this was the first node
                    self.the_table[idx] = node.next
                self.size -= 1  # decrement size
                print(f'value {node.value} has been removed')
                return True
            previous = node
            node = node.next  # keep going
        return False


# returns the value of the record with the matching key. If no record
# with matching key exists ->return None


    def search(self, key):
        hash_value = hash(key)
        idx = hash_value % self.cap
        node = self.the_table[idx]
        while (node):
            if (node.key == key):
                return node.value
            node = node.next  # keep going
        return None

    def capacity(self):
        print(f'the capacity of the table is: {self.cap}')
        return self.cap

    def __len__(self):
        print(f'the size of the table is: {self.size}')
        return self.size

    # def print(self):
    #     records_at_index =''
    #     for i in range(self.cap):
    #       records_at_index+=f' index {i}: '
    #       node = self.the_table[i]
    #       while (node):
    #           records_at_index+=f'{node.key}-->{node.value}-->'
    #           node = node.next
    #       records_at_index+="~empty~\n"
    #     print(records_at_index)
    #     return records_at_index


# ------driver code----
table = ChainingTable()  # create a new table
table.capacity()  # the capacity of the table is: 32
table.__len__()  # the size of the table is: 6

# new node with key 1 and value while has been inserted
table.insert(1, "while")
# new node with key 2 and value yellow has been inserted
table.insert(2, "yellow")
# new node with key 3 and value black has been inserted
table.insert(3, "black")
table.insert(4, "kiwi")  # new node with key 4 and value kiwi has been inserted
table.insert(5, "red")  # new node with key 3 and value black has been inserted
table.insert(6, "blue")  # new node with key 6 and value blue has been inserted
# # Search for a value
print(table.search(3))  # Output: black
table.modify(1, "pink")  # value while has been modified
print(table.search(1))  # Output: pink
table.remove(5)  # value red has been removed
print(table.search(5))  # None
# try to insert with a key that already exists
table.insert(2, "duplicate")  # key 2 already exists in the table
print(table.search(2))  # yellow ->original value
# try to insert to a key that has been removed
# new node with key 5 and value violet has been inserted
table.insert(5, "violet")
# search for a non existing key
print(table.search(300))  # None
table.capacity()  # the capacity of the table is: 32
table.__len__()  # the size of the table is: 6
# demonstrate doubling the table when load factor >1.0
table.insert(6, "blue")
table.insert(7, "blue")
table.insert(8, "blue")
table.insert(9, "blue")
table.insert(10, "blue")
table.insert(11, "blue")
table.insert(12, "blue")
table.insert(13, "blue")
table.insert(14, "blue")
table.insert(15, "blue")
table.insert(16, "blue")
table.insert(17, "blue")
table.insert(18, "blue")
table.insert(19, "blue")
table.insert(20, "blue")
table.insert(21, "blue")
table.insert(22, "blue")
table.insert(23, "blue")
table.insert(24, "blue")
table.insert(25, "blue")
table.insert(26, "blue")
table.insert(27, "blue")
table.insert(28, "blue")
table.insert(29, "blue")
table.insert(30, "blue")
table.insert(31, "blue")
table.insert(32, "blue")
table.capacity()  # the capacity of the table is: 32
table.__len__()  # the size of the table is: 32
# insert another value:
# load factor is larger than 1, adjusting table capacity
table.insert(33, "blue")
table.capacity()  # the capacity of the table is: 64 ***DOUBLE***
table.__len__()  # the size of the table is: 33

# display the table:
# table.print()
# index 0: 32-->blue-->~empty~
#  index 1: 33-->blue-->1-->pink-->~empty~
#  index 2: 2-->yellow-->~empty~
#  index 3: 3-->black-->~empty~
#  index 4: 4-->kiwi-->~empty~
#  index 5: 5-->violet-->~empty~
#  index 6: 6-->blue-->~empty~
#  index 7: 7-->blue-->~empty~
#  index 8: 8-->blue-->~empty~
#  index 9: 9-->blue-->~empty~
#  index 10: 10-->blue-->~empty~
#  index 11: 11-->blue-->~empty~
#  index 12: 12-->blue-->~empty~
#  index 13: 13-->blue-->~empty~
#  index 14: 14-->blue-->~empty~
#  index 15: 15-->blue-->~empty~
#  index 16: 16-->blue-->~empty~
#  index 17: 17-->blue-->~empty~
#  index 18: 18-->blue-->~empty~
#  index 19: 19-->blue-->~empty~
#  index 20: 20-->blue-->~empty~
#  index 21: 21-->blue-->~empty~
#  index 22: 22-->blue-->~empty~
#  index 23: 23-->blue-->~empty~
#  index 24: 24-->blue-->~empty~
#  index 25: 25-->blue-->~empty~
#  index 26: 26-->blue-->~empty~
#  index 27: 27-->blue-->~empty~
#  index 28: 28-->blue-->~empty~
#  index 29: 29-->blue-->~empty~
#  index 30: 30-->blue-->~empty~
#  index 31: 31-->blue-->~empty~
#  index 32: ~empty~
#  index 33: ~empty~
#  index 34: ~empty~
#  index 35: ~empty~
#  index 36: ~empty~
#  index 37: ~empty~
#  index 38: ~empty~
#  index 39: ~empty~
#  index 40: ~empty~
#  index 41: ~empty~
#  index 42: ~empty~
#  index 43: ~empty~
#  index 44: ~empty~
#  index 45: ~empty~
#  index 46: ~empty~
#  index 47: ~empty~
#  index 48: ~empty~
#  index 49: ~empty~
#  index 50: ~empty~
#  index 51: ~empty~
#  index 52: ~empty~
#  index 53: ~empty~
#  index 54: ~empty~
#  index 55: ~empty~
#  index 56: ~empty~
#  index 57: ~empty~
#  index 58: ~empty~
#  index 59: ~empty~
#  index 60: ~empty~
#  index 61: ~empty~
#  index 62: ~empty~
#  index 63: ~empty~
