
# ----------------------------------------------------------------------------------------------------------------------------------------

class SortedList:
    class Node:

        # Node is internal.  Feel free to add
        # to the argument list for its init function if you want
        # you can add additional data members if you like
        def __init__(self, data, next_=None, prev_=None):
            self.data = data
            self.next = next_
            self.prev = prev_

    # Sorted list is external, do not change its prototype.
    # you can add additional data members if you like
    def __init__(self):
        self.front = None
        self.back = None

# this function inserts data into the list such that the list stays sorted.
    def insert(self, data):
        new_node = self.Node(data)
        # case 1 - this is the first node in the list
        if self.front is None:
            self.front = new_node
            self.back = new_node
        # case 2 - this is going to be the starting node in the list
        elif self.front.data >= new_node.data:
            new_node.next = self.front
            new_node.next.prev = new_node
            self.front = new_node
        else:
            current = self.front
            # case 3 - this node belongs to the middle/end
            while (current.next is not None and current.next.data < new_node.data):
                current = current.next  # keep going
            new_node.next = current.next
            if current.next is not None:
                new_node.next.prev = new_node
            # all elements are smaller and we reached the end - insert at the END
            else:
                self.back = new_node
            current.next = new_node
            new_node.prev = current

#  this function finds and removes node containing data from the list.
#  If a node containing data was found and removed, function returns True.
#  If no such node was found (data was not in list), function returns False
#  note- if there are 2 identical nodes - will remove the first one

    def remove(self, data):
        found = self.is_present(data)
        if found:
            print("node found, deleting...")
            # option-1 : the node to delete is the first one
            if self.front.data == data:
                self.front = self.front.next
            # option-2: the node to delete is not the first one
            else:
                current = self.front
                while (current):
                    if current.data == data:
                        break
                    previous = current
                    current = current.next
                previous.next = current.next
            return True
        else:
            print(f'cannot delete, {data} doesn\'t exit in the current list')
        return False


# This function returns true, if data is in the list, false otherwise
    # same as linear search BUT since the list is sorted, may abort search when reached node>search_value


    def is_present(self, data):
        current = self.front
        while (current):
            if (current.data == data):
                return True
            elif (current.data > data):
                return False
            current = current.next
        return False

    def __len__(self):
        length = 0
        current = self.front
        while (current):
            length += 1
            current = current.next
        return length

        # print content, starting from the top
    def print(self):
        current = self.front
        while (current):  # traverse while there's is data in the current
            print(f'{current.data}', end="")
            current = current.next  # move forward to the next node
            print("---> ", end="")
        if not current:  # if current == None
            print("~END~")

    # The functions below called __iter__ and __reversed__
    # allows an external function to
    # iterate through your list.

    # with each iteration, curr goes through only one step of the while loop
    # (ie you don't run it all at once..)
    # there are two versions of these function as sentinels nodes do
    # make a difference in terms of where you start and end
    # keep only the version you are using and erase the version you are
    # not using (or comment it out...)

    # NOTE: if you change the names of your data members, you need
    # to change them in the functions below or your tests won't pass.

    # This is the version you need if you do not use sentinels:
    def __iter__(self):
        curr = self.front
        while curr:
            yield curr.data
            curr = curr.next

    def __reversed__(self):
        curr = self.back
        while curr:
            yield curr.data
            curr = curr.prev


# TESTING -
myll = SortedList()
myll.insert(6)
myll.insert(7)
myll.insert(70)
myll.insert(700)
myll.insert(100)
myll.insert(28)
myll.insert(56)
myll.insert(2)
myll.remove(2)
myll.remove(70)
myll.remove(6)

print("ascending")
for i in myll:
    print(i)

print("descending")

for i in reversed(myll):
    print(i)


dll = SortedList()
size = dll.__len__()
print(f'The size of the list is {size}')  # The size of the list is 0
dll.insert(30)
print(dll.is_present(30))  # True
dll.print()
print(f'The size of the list is {dll.__len__()}')  # The size of the list is 1
dll.insert(35)
dll.print()  # 30---> 35---> ~END~
print(f'The size of the list is {dll.__len__()}')  # The size of the list is 2
dll.insert(25)
dll.print()
print(f'The size of the list is {dll.__len__()}')
dll.insert(20)
dll.print()
print(f'The size of the list is {dll.__len__()}')
print(dll.is_present(22))  # False
print(dll.is_present(44))  # False
print(dll.is_present(20))  # True
print(dll.is_present(30))  # True
print(dll.is_present(35))  # True
dll.insert(21)
dll.print()  # 20---> 21---> 25---> 30---> 35---> ~END~
dll.insert(33)
dll.print()  # 20---> 21---> 25---> 30---> 33---> 35---> ~END~
dll.insert(24)
dll.insert(23)
dll.insert(23)
dll.insert(34)
dll.insert(36)
dll.insert(19)
dll.insert(100)
dll.insert(99)
dll.print()  # 19---> 20---> 21---> 23---> 23---> 24---> 25---> 30---> 33---> 34---> 35---> 36---> 99---> 100---> ~END~
print(dll.__len__())  # 14
dll.remove(19)  # remove the first node
dll.print()  # 20---> 21---> 23---> 23---> 24---> 25---> 30---> 33---> 34---> 35---> 36---> 99---> 100---> ~END~
print(dll.__len__())  # 13
dll.remove(100)  # remove the last node
dll.print()  # 20---> 21---> 23---> 23---> 24---> 25---> 30---> 33---> 34---> 35---> 36---> 99---> ~END~
dll.remove(24)  # remove from the middle
dll.print()  # 20---> 21---> 23---> 23---> 25---> 30---> 33---> 34---> 35---> 36---> 99---> ~END~
dll.remove(36)
dll.print()  # 20---> 21---> 23---> 23---> 25---> 30---> 33---> 34---> 35---> 99---> ~END~
dll.insert(36)
dll.print()  # 20---> 21---> 23---> 23---> 25---> 30---> 33---> 34---> 35---> 36---> 99---> ~END~
dll.insert(35)  # now we  have 2 35!
print(dll.is_present(35))  # True
dll.remove(35)  # node found, deleting...
dll.print()
print(dll.is_present(35))  # True -there is another one
dll.remove(20)
dll.remove(99)
dll.remove(25)
dll.remove(23)
dll.remove(34)
dll.remove(36)
dll.remove(35)
dll.print()  # cannot delete, 35 doesn't exit in the current list
dll.remove(35)  # cannot delete, 35 doesn't exit in the current list
dll.remove(23)
dll.remove(30)
dll.remove(33)
dll.print()  # 21---> ~END~
dll.remove(21)
dll.print()  # ~END~
