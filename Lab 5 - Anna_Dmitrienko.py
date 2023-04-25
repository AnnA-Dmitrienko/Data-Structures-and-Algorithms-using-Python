# Lab-5, DSA456V1a
# Student name: Anna Dmitrienko
# Student ID - 120-412-218
# Email - admitrienko@myseneca.ca
# ----------------------------------------------------------------------------------------------------------------------------------------

# In this exercise, I will create a singly linked list of unsigned ints
# My list will contain methods to manipulate it, such as inserting and removing values,
# as well as searching through the list and printing its content


class Node:
    # initialize node obj
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node  # next node constructed with null by default


class SinglyLinkedList:

    # initialize the head
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head  # returns TRUE is the list is empty

    # inserts a new node containing data at the BEGINNING of the list
    def prepend(self, data):
        # create a new node with the data we want to insert
        new_node = Node(data)
        # check if this was the first node
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node  # connect the head with the new node

    # inserts a new node containing data at the END of the list

    def append(self, data):
        new_node = Node(data)
        # check for special case - this is the first node in the list:
        if self.is_empty():
            self.head = new_node
        else:
            # traverse the list, find last element and insert it there
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node  # we reached the end of the list

    # inserts a new node containing data after the node target-INCORRECT THE TARGET IS GIVEN! NO NEED TO CHECK IF ITS THERE

    def insert_after(self, target, data):
        # first we'll check  if the list is not empty
        if self.is_empty():
            print("the list is empty, cannot perform operation of inserting AFTER....")
            return
        # second we'll check if the node target exists in the list
        found = self.search(target)
        if found:
            print(f'node found, inserting {data} after {target}')
            new_node = Node(data)
            current = self.head
            while (current):
                if current.data == target:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
        else:
            print(f'cannot insert, {target} is not found in the list')
        return

    # deletes the node target from the list
    # ASSUMPTION- each node.data is unique
    # If there are 2 identical nodes, will delete the first one from the head

    def delete(self, target):
        found = self.search(target)
        if found:
            print("node found, deleting...")
            # option-1 : the node to delete is the first one
            if self.head.data == target:
                self.head = self.head.next
            # option-2: the node to delete is not the first one
            else:
                current = self.head
                while (current):
                    if current.data == target:
                        break
                    previous = current
                    current = current.next
                previous.next = current.next
            return True
        else:
            print(f'{target} doesn\'t exit in the current list')
        return False

    # search for a node, return it if found, None - if not

    def search(self, data):
        current = self.head
        while (current):
            if (current.data == data):  # if the data in the current is the same as we are looking for
                return current.data
            current = current.next  # keep looking
        return None

    # traverse the list and find its size
    def size(self):
        size = 0
        current = self.head
        while (current):
            size += 1
            current = current.next
        return size

    # returns a list containing traversed data in the linked list
    def to_list(self):
        # create an empty list
        ll_list = []
        current = self.head
        while (current):
            ll_list.append(current.data)
            current = current.next
        return ll_list

    # print content, starting from the head
    def print(self):
        current = self.head
        while (current):  # traverse while there's is data in the current
            print(f'{current.data}', end="")
            current = current.next  # move forward to the next node
            print("---> ", end="")
        if not current:  # if current == None
            print("~END~")


# ***********************************************************************************************************************************
# driver code
# initialize an empty list
ll = SinglyLinkedList()

print(ll.is_empty())  # True
print(ll.size())  # 0

# prepend a value
ll.prepend(5)
ll.print()  # 5---> ~END~
print(ll.is_empty())  # False
print(ll.size())  # 1

ll.prepend(10)
ll.print()  # 10---> 5---> ~END~
print(ll.size())  # 2

ll.delete(5)  # node found, deleting...
print(ll.size())  # 1
ll.delete(10)  # node found, deleting...
ll.print()  # ~END~
print("END OF TEST1- PREPEND")
# append a value
ll.append(50)
ll.print()  # 50---> ~END~
print(ll.is_empty())  # False
print(ll.size())  # 1

ll.append(100)
ll.print()  # 50---> 100---> ~END~
print(ll.size())  # 2

ll.delete(5)  # 5 doesn't exit in the current list
print(ll.size())  # 2
ll.delete(50)  # node found, deleting...
ll.delete(100)  # node found, deleting...
ll.print()  # ~END~
print("END OF TEST2- APPEND")

# insert after
# the list is empty, cannot perform operation of inserting AFTER....
ll.insert_after(5, 10)
ll.append(500)
ll.insert_after(500, 200)
ll.print()
ll.prepend(30)
ll.append(40)
ll.insert_after(40, 60)  # node found, inserting 60 after 40
ll.print()  # 30---> 500---> 200---> 40---> 60---> ~END~
print(ll.size())  # 5
print(ll.is_empty())  # False
print("END OF TEST3- INSERT AFTER")

print(ll.search(200))  # 200
ll.delete(200)  # node found, deleting...
print(ll.search(200))  # None
print(ll.search(30))  # 30
print(ll.search(60))  # 60
print("END OF TEST4- SEARCH")

print(ll.to_list())  # [30, 500, 40, 60]
ll.delete(30)  # node found, deleting...
ll.delete(60)  # node found, deleting..
ll.delete(40)  # node found, deleting..
ll.delete(500)  # node found, deleting..
print(ll.to_list())  # []
ll.append(50)
ll.append(50)
ll.append(50)
ll.print()  # 50---> 50---> 50---> ~END~
ll.delete(50)  # node found, deleting...
ll.print()  # 50---> 50---> ~END~
