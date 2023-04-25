

# Function -1
'''
This function is passed a number and returns
(number)(number-1)(number-2)...(3)(2)(1). By definition, 0! = 1
'''

# Assumption- number can only be unsigned integer


def factorial(number):
    returnValue = 1  # for cases number is 0 or 1
    if (number > 1):
        returnValue = number*factorial(number-1)
    return returnValue


# TESTING :
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(2))  # 2
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(23))  # 25852016738884976640000
print('end func1')
print('=======================================')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function -2
'''
Write the RECURIVE function linear_search. linear_search() is passed a list of values and a key.
If a matching key is found in the list, function returns index of where the key was found. 
If the key is not found, function returns -1.
'''

# Solution-1: writing recursive function separately


def linear_search_rec(list, key, firstIndex, lastIndex):
    if firstIndex > lastIndex:  # no items left in the list
        return -1
    if (list[firstIndex] == key):
        return firstIndex
    else:
        return linear_search_rec(list, key, firstIndex+1, lastIndex)


def linear_search(list, key):
    return linear_search_rec(list, key, 0, len(list)-1)


# TESTING :
print(linear_search([1, 2, 3, -5, 6, -10, 21, 40], 6))  # found at index=4
print(linear_search([1, 2, 3, 5, 6, 10, 21, 40], 2))  # found at index=1
# return -1 =>not found
print(linear_search([1, 2, -3, 5, 6, 10, -21, 40], 7))
# return -1 => not found
print(linear_search([1, -2, 3, 5, 6, 10, 21, -40], 40))
print('end func2 linear search solution-I (professor)')
print('=======================================')


# Solution-2 : with 3 parameters
def linear_search2(list, key, size):
    if (size <= 0):
        return -1
    elif (list[size-1] == key):  # compare the last element
        return size-1        # return its index if there's a match
    # added the parameter size, so the function will start from last element and move step-by-step to the first
    return linear_search2(list, key, size-1)


# TESTING :
print(linear_search2([1, 2, 3, -5, 6, -10, 21, 40], 6, 8))  # found at index=4
print(linear_search2([1, 2, 3, 5, 6, 10, 21, 40], 2, 8))  # found at index=1
# return -1 =>not found
print(linear_search2([1, 2, -3, 5, 6, 10, -21, 40], 7, 8))
# return -1 => not found
print(linear_search2([1, -2, 3, 5, 6, 10, 21, -40], 40, 8))
print('end func2 linear search solution-II (Anna)')
print('=======================================')


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function -3
'''
Write the RECURIVE function binary_search. binary_search() is passed a sorted list of values and a key. 
If a matching key is found in the list, function returns index of where the key was found. 
If the key is not found, function returns -1.
'''


# Assumption - the list is pre-sorted
# Solution-1: writing recursive function separately

def binary_search_rec(list, key, firstIndex, lastIndex):
    if firstIndex > lastIndex:
        return -1
    mid = (firstIndex+lastIndex)//2
    if list[mid] == key:
        return mid
    elif list[mid] > key:
        return binary_search_rec(list, key, firstIndex, mid-1)
    # the other option is list[mid]<key
    return binary_search_rec(list, key, mid+1, lastIndex)


def binary_search(list, key):
    return binary_search_rec(list, key, 0, len(list)-1)


# TESTING :
print(binary_search([1, 2, 3, 5, 6, 10], 6))  # found at index=4
print(binary_search([1, 2, 3, 5, 6, 10], 100))  # not found => -1
print(binary_search([-2, -1], -1))   # found at index=1
print(binary_search([1, 1], 1))   # found at index=0
print(binary_search([2], 1))   # not found => -1
print('end func3 solution-I')
print('=======================================')


# Solution-2 : just one function with 4 parameters
def binary_search2(list, key, firstIndex, lastIndex):
    if (firstIndex <= lastIndex):
        mid = (firstIndex+lastIndex)//2  # integer division
        if (key == list[mid]):
            return mid  # if item found return its index
        elif (key < list[mid]):
            # narrow the search by looking at the low end
            return binary_search2(list, key, firstIndex, mid-1)
        elif (key > list[mid]):
            # narrow the search by looking at the high end
            return binary_search2(list, key, mid+1, lastIndex)
    return -1


# TESTING :
print(binary_search2([1, 2, 3, 5, 6, 10], 6, 0, 5))  # found at index=4
print(binary_search2([1, 2, 3, 5, 6, 10], 100, 0, 5))  # not found => -1
print(binary_search2([-2, -1], -1, 0, 1))   # found at index=1
print(binary_search2([1, 1], 1, 0, 1))   # found at index=0
print(binary_search2([2], 1, 0, 0))   # not found => -1
print('end func3 solution-II with 4 params')
print('=======================================')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function -4

'''Whrite a recusrive program that gets the number of disks on tower 1 and lists all the moves to take them to tower 3 using tower 2.
 The moves should be like:
1 to 2 (which means the top disk on tower 1 should be moved to tower 2)
1 to 3
2 to 3'''


# Base caw 1 disks
# Base case 2 disks
# Assumption - number passed is an unsigned int
# move n-1 disks from source to the middle point, move the base disk from source to destination (1opertion)
# then move n-1 disks from mid to destination


def hanoi(number, start, middle, end):
    if number == 1:
        return print(f'from {start} to {end}\n')
    else:
        # solve for n-1 disks - place them in the middle to free the lowest disk
        hanoi(number-1, start, end, middle)
        # move lower disk from start to end -base case
        print(f'from {start} to {end}\n')
        # move rest of the disks from the middle to their destination
        hanoi(number-1, middle, start, end)


print('Hanoi moves:')
hanoi(1, 'start', 'middle', 'end')
print('=======================================')

print('Hanoi moves:')
hanoi(2, 'start', 'middle', 'end')
print('=======================================')

print('Hanoi moves:')
hanoi(3, 'start', 'middle', 'end')
print('=======================================')

# calculate #of operations to move the disks


def hanoi_towers(number):
    if number == 1:
        return 1
    else:
        return 2*hanoi_towers(number-1)+1


# TESTING :
print(hanoi_towers(1))  # 1
print(hanoi_towers(2))  # 3
print(hanoi_towers(3))  # 7
print(hanoi_towers(4))  # 15
print(hanoi_towers(5))  # 31
print(hanoi_towers(6))  # 63
print(hanoi_towers(7))  # 127
print('end func4')
