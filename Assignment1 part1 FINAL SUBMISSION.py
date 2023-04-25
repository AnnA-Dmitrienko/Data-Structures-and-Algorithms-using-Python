#!/usr/bin/env python
# coding: utf-8

# In[1]:

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Part-1


# In[153]:


# importing the required modules
import matplotlib.pyplot as plt
import random
import time
import math


# In[154]:


# bubble sort
def bubble_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                steps += 4  # 4 operations, 3 for swap, 1 for comparison
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return steps


# In[155]:


# selection sort
def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        min_idx = i  # record the index of the smallest value, initialized with where the smallest value may be found
        for j in range(i + 1, n):              # go through list,
            if my_list[j] < my_list[min_idx]:  # and every time we find a smaller value,
                steps += 1  # 1 operation for comparison
                # record its index (note how nothing has moved at this point.)
                min_idx = j
                steps += 1  # 1 operation for comparison
        if min_idx != i:
            steps += 3  # 3 operations for swap
            my_list[min_idx], my_list[i] = my_list[i], my_list[min_idx]
    return steps


# In[156]:


# insertion sort
def insertion_sort(my_list):
    steps = 0
    for i in range(1, len(my_list)):
        curr = my_list[i]  # store the first number in the unsorted part of
        # of array into curr
        j = i
        # this loop shifts value within sorted part of array
        while j > 0 and my_list[j - 1] > curr:
            steps += 1  # 1 operation for comparison
            my_list[j] = my_list[j - 1]              # to open a spot for curr
            j -= 1
            steps += 3  # increment steps for the swap
        my_list[j] = curr
    return steps


# In[157]:


# merge sort
def merge(mylist, a_first_index, b_first_index, b_last_index, empty_list):
    steps = 0
    a_ptr = a_first_index
    b_ptr = b_first_index
    empty_list_index = a_ptr

    while (a_ptr < b_first_index) and (b_ptr <= b_last_index):
        steps += 1  # 1 operation for comparison
        if mylist[a_ptr] <= mylist[b_ptr]:
            steps += 1  # 1 operation for moving value to empty list
            empty_list[empty_list_index] = mylist[a_ptr]
            empty_list_index += 1
            a_ptr += 1
        else:
            steps += 1  # 1 operation for moving value to empty list
            empty_list[empty_list_index] = mylist[b_ptr]
            empty_list_index += 1
            b_ptr += 1

    while a_ptr < b_first_index:
        steps += 1  # 1 operation for comparison
        empty_list[empty_list_index] = mylist[a_ptr]
        empty_list_index += 1
        a_ptr += 1

    while b_ptr <= b_last_index:
        steps += 1  # 1 operation for comparison
        empty_list[empty_list_index] = mylist[b_ptr]
        empty_list_index += 1
        b_ptr += 1

    for i in range(a_first_index, b_last_index + 1):
        mylist[i] = empty_list[i]
    return steps


def recursive_merge_sort(mylist, first_index, last_index, empty_list):
    steps = 0
    recurRHS = 0
    recurLHS = 0
    merging = 0

    if first_index < last_index:
        steps += 1  # 1 operation for comparison
        mid_index = (first_index + last_index) // 2
        recurLHS = recursive_merge_sort(
            mylist, first_index, mid_index, empty_list)
        recurRHS = recursive_merge_sort(
            mylist, mid_index + 1, last_index, empty_list)
        merging = merge(mylist, first_index, mid_index +
                        1, last_index, empty_list)
    return steps + recurRHS + recurLHS + merging


def merge_sort(mylist):
    steps = 0
    # create an empty list for merging.  doing it once
    empty_list = [0] * len(mylist)
    # is more efficient than repeatedly creating it when merging

    steps = recursive_merge_sort(mylist, 0, len(
        mylist) - 1, empty_list)  # call recursive mergesort
    return steps


# In[158]:


# quick sort
def insertion_sort_for_quick(mylist, left, right):
    steps = 0
    for i in range(left + 1, right + 1):
        curr = mylist[i]  # store the first number in the unsorted part of
        # of array into curr
        j = i
        # this loop shifts value within sorted part of array to open a spot for curr
        while j > left and mylist[j - 1] > curr:
            steps += 1  # 1 operation for comparison
            mylist[j] = mylist[j - 1]
            steps += 3  # increment steps for the swap
            j = j - 1
        mylist[j] = curr
    return steps


def partition(mylist, left, right):
    steps_partition = 0
    # choose a random index between left and right inclusive
    pivot_location = random.randint(left, right)

    # get the pivot
    pivot = mylist[pivot_location]

    # move the pivot out of the way by swapping with
    # last value of partition.  This step is crucial as pivot will
    # end up "moving" if we don't get it out of the way which will
    # lead to inconsistent results.
    mylist[pivot_location] = mylist[right]
    mylist[right] = pivot

    end_of_smaller = left - 1

    # note the loop below does not look at pivot which is in mylist[right]
    for j in range(left, right):
        if mylist[j] <= pivot:
            steps_partition += 1  # 1 operation for comparison
            end_of_smaller += 1
            mylist[end_of_smaller], mylist[j] = mylist[j], mylist[end_of_smaller]
            steps_partition += 3  # 3 operations for swap

    # restore the pivot
    mylist[end_of_smaller +
           1], mylist[right] = mylist[right], mylist[end_of_smaller + 1]
    steps_partition += 3  # 3 operations for swap

    pivot_position = end_of_smaller+1

    # and return its location
    return pivot_position, steps_partition


def recursive_quick_sort(mylist, left, right, THRESHOLD=32):
    steps = 0
    insertion_steps = 0
    recurRHS = 0
    recurLHS = 0
    steps_partition = 0

    if right - left <= THRESHOLD:
        steps += 1  # 1 operation for comparison
        insertion_steps = insertion_sort_for_quick(mylist, left, right)
    else:
        steps += 1  # 1 operation for comparison (else case)
        pivot_position, steps_partition = partition(mylist, left, right)
        # pivot_position = partition(mylist, left, right)
        recurRHS = recursive_quick_sort(mylist, left, pivot_position - 1)
        recurLHS = recursive_quick_sort(mylist, pivot_position + 1, right)
    return steps + insertion_steps + recurRHS + recurLHS + steps_partition


def quick_sort(mylist):
    steps = 0
    steps = recursive_quick_sort(mylist, 0, len(
        mylist) - 1)  # call recursive quicksort
    return steps


# In[165]:


def main():

    # 1. BUBBLE SORT

    print("~~~BUBBLE SORT CALCULATIONS~~~")

    # step-1
    # creating a random list of 100 elements
    list_100 = 100
    random_100_bubble = [random.randint(0, 300) for val in range(list_100)]
    print(f'list before sorting: {random_100_bubble}\n')

    # test the algorithm
    bubble_sort(random_100_bubble)
    print(
        f'list after applying bubble_sort on random 100 numbers: {random_100_bubble}\n')

    # step-2 : add lines of code...added in the above function

    # test T(n) calculation

    # 1. Best case scenario - values already sorted
    list_50 = 50
    random_50_bubble = [random.randint(0, 300) for val in range(list_50)]
    random_50_bubble.sort()
    print(random_50_bubble)
    print(
        f'steps needed for sorting Best Case: {bubble_sort(random_50_bubble)}\n')
    '''Best case T(n) is O(n), still makes one comparison with each pair of elements, 
    but goes through the loop once'''

    # 2. Worst case scenario - values in reversed order (descending)
    random_50_bubble.sort(reverse=True)
    print(random_50_bubble)
    print(
        f'steps needed for sorting Worst Case: {bubble_sort(random_50_bubble)}\n')
    '''Worst case T(n) is O(n^2)'''

    # 3. Average case scenario - for the average case about half of the values needed to be sorted
    # I will create a random list of 50 elements to test
    random_50_average_bubble = [
        random.randint(0, 300) for val in range(list_50)]
    print(random_50_average_bubble)
    print(
        f'steps needed for sorting Average Case: {bubble_sort(random_50_average_bubble)}\n')
    '''Average case T(n) is O(n^2)'''

    # step-3
    # plot T(n) vs n

    # x-axis: number of elements
    # y-axis: T(n) calculation

    size10 = 10
    size50 = 50
    size100 = 100
    size500 = 500
    size1000 = 1000
    size5000 = 5000
    size10000 = 10000
    size50000 = 50000
    size100000 = 100000
    size_million = 1000000

    # creating lists for worst cases
    ran10_bubble = [random.randint(0, 1000000) for val in range(size10)]
    ran10_bubble.sort(reverse=True)
    # print(ran10_bubble) - testing - prints a random list in range 0-1M reversed order
    # print(bubble_sort(ran10_bubble)) - testing - returns T(n) in this case result: 180

    ran50_bubble = [random.randint(0, 1000000) for val in range(size50)]
    ran50_bubble.sort(reverse=True)

    ran100_bubble = [random.randint(0, 1000000) for val in range(size100)]
    ran100_bubble.sort(reverse=True)

    ran500_bubble = [random.randint(0, 1000000) for val in range(size500)]
    ran500_bubble.sort(reverse=True)

    ran1000_bubble = [random.randint(0, 1000000) for val in range(size1000)]
    ran1000_bubble.sort(reverse=True)

    ran5000_bubble = [random.randint(0, 1000000) for val in range(size5000)]
    ran5000_bubble.sort(reverse=True)
    # print(bubble_sort(ran5000_bubble)) - result: 49989960

    '''
    I get an error on these values - my computer is not strong enough to deal with this complexity 
    
    ran10000_bubble = [random.randint(0,1000000) for val in range (size10000)]
    ran10000_bubble.sort(reverse=True)
    
    ran50000_bubble = [random.randint(0,1000000) for val in range (size50000)]
    ran50000_bubble.sort(reverse=True)
    
    ran100000_bubble = [random.randint(0,1000000) for val in range (size100000)]
    ran100000_bubble.sort(reverse=True)
    
    ran1000000_bubble = [random.randint(0,1000000) for val in range (size_million)]
    ran1000000_bubble.sort(reverse=True)
    
    '''

    # sort the arrays, measure number of operations (for step3) and time (for step4)
    # convert the time to milliseconds
    time_start_bubble_10 = round(time.time()*1000)
    bubble_sorted10 = bubble_sort(ran10_bubble)
    time_end_bubble_10 = round(time.time()*1000)
    diff_bubble_10 = time_end_bubble_10 - time_start_bubble_10

    time_start_bubble_50 = round(time.time()*1000)
    bubble_sorted50 = bubble_sort(ran50_bubble)
    time_end_bubble_50 = round(time.time()*1000)
    diff_bubble_50 = time_end_bubble_50 - time_start_bubble_50

    time_start_bubble_100 = round(time.time()*1000)
    bubble_sorted100 = bubble_sort(ran100_bubble)
    time_end_bubble_100 = round(time.time()*1000)
    diff_bubble_100 = time_end_bubble_100 - time_start_bubble_100

    time_start_bubble_500 = round(time.time()*1000)
    bubble_sorted500 = bubble_sort(ran500_bubble)
    time_end_bubble_500 = round(time.time()*1000)
    diff_bubble_500 = time_end_bubble_500 - time_start_bubble_500

    time_start_bubble_1000 = round(time.time()*1000)
    bubble_sorted1000 = bubble_sort(ran1000_bubble)
    time_end_bubble_1000 = round(time.time()*1000)
    diff_bubble_1000 = time_end_bubble_1000 - time_start_bubble_1000
    # print(diff_bubble_1000) # result - 145 ms

    time_start_bubble_5000 = round(time.time()*1000)
    bubble_sorted5000 = bubble_sort(ran5000_bubble)
    time_end_bubble_5000 = round(time.time()*1000)
    diff_bubble_5000 = time_end_bubble_5000 - time_start_bubble_5000
    # print(diff_bubble_5000) # result - 3699 ms

    # create X and Y values for the scatter plot
    n_elem_bubble = [10, 50, 100, 500, 1000, 5000]
    Tn_bubble = [bubble_sorted10, bubble_sorted50, bubble_sorted100,
                 bubble_sorted500, bubble_sorted1000, bubble_sorted5000]

    # plot the values
    plt.scatter(n_elem_bubble, Tn_bubble, c="blue")

    # add namings
    plt.title('Bubble Sort: T(n) vs (n)')
    plt.xlabel("number of elements")
    plt.ylabel("number of operations (le7)")

    # To show the plot
    plt.show()
    '''
    As appears from the graph,  T(n) vs (n) in Bubble Sort is O(n^2) complexity.
    We see that the curve is aligned with what we learned about the performance of bubble sort. 
    '''

    # step-4
    # plot time to perform the algorithm against number of elements

    time_bubble = [diff_bubble_10, diff_bubble_50, diff_bubble_100,
                   diff_bubble_500, diff_bubble_1000, diff_bubble_5000]

    # plot the values
    plt.scatter(n_elem_bubble, time_bubble, c="green")

    # add namings
    plt.title('Bubble Sort: Time vs (n)')
    plt.xlabel("number of elements")
    plt.ylabel("number of operations (milliseconds)")

    # To show the plot
    plt.show()

    '''As with the graph in step 3, we can see a quadratic O(n²) time complexity.
    We see that the curve is aligned with what we learned about the performance of bubble sort. 
    '''

    print("*****************************************************************************************************************")

    print("~~~SELECTION SORT CALCULATIONS~~~")

    # step-1
    # creating a random list of 100 elements
    random_100_selection = [random.randint(0, 300) for val in range(list_100)]
    print(f'list before sorting: {random_100_selection}\n')

    # test the algorithm
    selection_sort(random_100_selection)
    print(
        f'list after applying selection_sort on random 100 numbers: {random_100_selection}\n')

    # step-2 : add lines of code...added in the above function

    # test T(n) calculation

    # 1. Best case scenario - values already sorted
    random_50_selection = [random.randint(0, 300) for val in range(list_50)]
    random_50_selection.sort()
    print(random_50_selection)
    print(
        f'steps needed for sorting Best Case: {selection_sort(random_50_selection)}\n')
    '''Best case T(n) is O(n^2) still have to iterate n^2 times to validate 
    that the minimum value is in the correct index. So even pre-sorting the values doesnt help'''

    # 2. Worst case scenario - values in reversed order (descending)
    random_50_selection.sort(reverse=True)
    print(random_50_selection)
    print(
        f'steps needed for sorting Worst Case: {selection_sort(random_50_selection)}\n')
    '''Worst case T(n) is O(n^2)'''

    # 3. Average case scenario - for the average case about half of the values needed to be sorted
    # I will create a random list of 50 elements to test
    random_50_average_selection = [
        random.randint(0, 300) for val in range(list_50)]
    print(random_50_average_selection)
    print(
        f'steps needed for sorting Average Case: {selection_sort(random_50_average_selection)}\n')
    '''Average case T(n) is O(n^2)'''

    # step-3
    # plot T(n) vs n

    # x-axis: number of elements
    # y-axis: T(n) calculation

    # creating lists for worst cases
    ran10_selection = [random.randint(0, 1000000) for val in range(size10)]
    ran10_selection.sort(reverse=True)
    # print(ran10_selection) # - testing - prints a random list in range 0-1M reversed order
    # print(selection_sort(ran10_selection))# - testing - returns T(n) in this case result: 79

    ran50_selection = [random.randint(0, 1000000) for val in range(size50)]
    ran50_selection.sort(reverse=True)

    ran100_selection = [random.randint(0, 1000000) for val in range(size100)]
    ran100_selection.sort(reverse=True)

    ran500_selection = [random.randint(0, 1000000) for val in range(size500)]
    ran500_selection.sort(reverse=True)

    ran1000_selection = [random.randint(0, 1000000) for val in range(size1000)]
    ran1000_selection.sort(reverse=True)

    ran5000_selection = [random.randint(0, 1000000) for val in range(size5000)]
    ran5000_selection.sort(reverse=True)
    # print(selection_sort(ran5000_selection)) #- result: 12497555

    # sort the arrays, measure number of operations (for step3) and time (for step4)
    # convert the time to milliseconds
    time_start_selection_10 = round(time.time()*1000)
    selection_sorted10 = selection_sort(ran10_selection)
    time_end_selection_10 = round(time.time()*1000)
    diff_selection_10 = time_end_selection_10 - time_start_selection_10

    time_start_selection_50 = round(time.time()*1000)
    selection_sorted50 = selection_sort(ran50_selection)
    time_end_selection_50 = round(time.time()*1000)
    diff_selection_50 = time_end_selection_50 - time_start_selection_50

    time_start_selection_100 = round(time.time()*1000)
    selection_sorted100 = selection_sort(ran100_selection)
    time_end_selection_100 = round(time.time()*1000)
    diff_selection_100 = time_end_selection_100 - time_start_selection_100

    time_start_selection_500 = round(time.time()*1000)
    selection_sorted500 = selection_sort(ran500_selection)
    time_end_selection_500 = round(time.time()*1000)
    diff_selection_500 = time_end_selection_500 - time_start_selection_500

    time_start_selection_1000 = round(time.time()*1000)
    selection_sorted1000 = selection_sort(ran1000_selection)
    time_end_selection_1000 = round(time.time()*1000)
    diff_selection_1000 = time_end_selection_1000 - time_start_selection_1000
    # print(diff_selection_1000) # result - 55 ms

    time_start_selection_5000 = round(time.time()*1000)
    selection_sorted5000 = selection_sort(ran5000_selection)
    time_end_selection_5000 = round(time.time()*1000)
    diff_selection_5000 = time_end_selection_5000 - time_start_selection_5000
    # print(diff_selection_5000) # result - 1375 ms

    # create X and Y values for the scatter plot
    n_elem_selection = [10, 50, 100, 500, 1000, 5000]
    Tn_selection = [selection_sorted10, selection_sorted50, selection_sorted100,
                    selection_sorted500, selection_sorted1000, selection_sorted5000]

    # plot the values
    plt.scatter(n_elem_selection, Tn_selection, c="blue")

    # add namings
    plt.title('Selection Sort: T(n) vs (n)')
    plt.xlabel("number of elements")
    plt.ylabel("number of operations (le7)")

    # To show the plot
    plt.show()
    '''
    As appears from the graph,  T(n) vs (n) in Selection Sort is O(n^2) complexity.
    We see that the curve is aligned with what we learned about the performance of selection sort. 
    '''

    # step-4
    # plot time to perform the algorithm against number of elements

    time_selection = [diff_selection_10, diff_selection_50, diff_selection_100,
                      diff_selection_500, diff_selection_1000, diff_selection_5000]

    # plot the values
    plt.scatter(n_elem_selection, time_selection, c="green")

    # add namings
    plt.title('selection Sort: Time vs (n)')
    plt.xlabel("number of elements")
    plt.ylabel("number of operations (milliseconds)")

    # To show the plot
    plt.show()

    '''As with the graph in step 3, we can see a quadratic O(n²) time complexity.
    We see that the curve is aligned with what we learned about the performance of selection sort. 
    '''

    print("*****************************************************************************************************************")

    print("~~~INSERTION SORT CALCULATIONS~~~")

    # step-1
    # creating a random list of 100 elements
    random_100_insertion = [random.randint(0, 300) for val in range(list_100)]
    print(f'list before sorting: {random_100_insertion}\n')

    # test the algorithm
    insertion_sort(random_100_insertion)
    print(
        f'list after applying insertion_sort on random 100 numbers: {random_100_insertion}\n')

    # step-2 : add lines of code...added in the above function

    # test T(n) calculation

    # 1. Best case scenario - values already sorted
    random_50_insertion = [random.randint(0, 300) for val in range(list_50)]
    random_50_insertion.sort()
    print(random_50_insertion)
    print(
        f'steps needed for sorting Best Case: {insertion_sort(random_50_insertion)}\n')
    '''Best case T(n) is O(n), still have to go trough the values once
    to validate they are in correct positions'''

    # 2. Worst case scenario - values in reversed order (descending)
    random_50_insertion.sort(reverse=True)
    print(random_50_insertion)
    print(
        f'steps needed for sorting Worst Case: {insertion_sort(random_50_insertion)}\n')
    '''Worst case T(n) is O(n^2)'''

    # 3. Average case scenario - for the average case about half of the values needed to be sorted
    # I will create a random list of 50 elements to test
    random_50_average_insertion = [
        random.randint(0, 300) for val in range(list_50)]
    print(random_50_average_insertion)
    print(
        f'steps needed for sorting Average Case: {insertion_sort(random_50_average_insertion)}\n')
    '''Average case T(n) is O(n^2)'''

    # step-3
    # plot T(n) vs n

    # x-axis: number of elements
    # y-axis: T(n) calculation

    # creating lists for worst cases
    ran10_insertion = [random.randint(0, 1000000) for val in range(size10)]
    ran10_insertion.sort(reverse=True)
    # print(ran10_insertion) # - testing - prints a random list in range 0-1M reversed order
    # print(insertion_sort(ran10_insertion))# - testing - returns T(n) in this case result: 180

    ran50_insertion = [random.randint(0, 1000000) for val in range(size50)]
    ran50_insertion.sort(reverse=True)

    ran100_insertion = [random.randint(0, 1000000) for val in range(size100)]
    ran100_insertion.sort(reverse=True)

    ran500_insertion = [random.randint(0, 1000000) for val in range(size500)]
    ran500_insertion.sort(reverse=True)

    ran1000_insertion = [random.randint(0, 1000000) for val in range(size1000)]
    ran1000_insertion.sort(reverse=True)

    ran5000_insertion = [random.randint(0, 1000000) for val in range(size5000)]
    ran5000_insertion.sort(reverse=True)
    # print(insertion_sort(ran5000_insertion)) #- result: 49989964

    # sort the arrays, measure number of operations (for step3) and time (for step4)
    # convert the time to milliseconds
    time_start_insertion_10 = round(time.time()*1000)
    insertion_sorted10 = insertion_sort(ran10_insertion)
    time_end_insertion_10 = round(time.time()*1000)
    diff_insertion_10 = time_end_insertion_10 - time_start_insertion_10

    time_start_insertion_50 = round(time.time()*1000)
    insertion_sorted50 = insertion_sort(ran50_insertion)
    time_end_insertion_50 = round(time.time()*1000)
    diff_insertion_50 = time_end_insertion_50 - time_start_insertion_50

    time_start_insertion_100 = round(time.time()*1000)
    insertion_sorted100 = insertion_sort(ran100_insertion)
    time_end_insertion_100 = round(time.time()*1000)
    diff_insertion_100 = time_end_insertion_100 - time_start_insertion_100

    time_start_insertion_500 = round(time.time()*1000)
    insertion_sorted500 = insertion_sort(ran500_insertion)
    time_end_insertion_500 = round(time.time()*1000)
    diff_insertion_500 = time_end_insertion_500 - time_start_insertion_500

    time_start_insertion_1000 = round(time.time()*1000)
    insertion_sorted1000 = insertion_sort(ran1000_insertion)
    time_end_insertion_1000 = round(time.time()*1000)
    diff_insertion_1000 = time_end_insertion_1000 - time_start_insertion_1000
    # print(diff_insertion_1000) # result - 145 ms

    time_start_insertion_5000 = round(time.time()*1000)
    insertion_sorted5000 = insertion_sort(ran5000_insertion)
    time_end_insertion_5000 = round(time.time()*1000)
    diff_insertion_5000 = time_end_insertion_5000 - time_start_insertion_5000
    # print(diff_insertion_5000) # result - 3676 ms

    # create X and Y values for the scatter plot
    n_elem_insertion = [10, 50, 100, 500, 1000, 5000]
    Tn_insertion = [insertion_sorted10, insertion_sorted50, insertion_sorted100,
                    insertion_sorted500, insertion_sorted1000, insertion_sorted5000]

    # plot the values
    plt.scatter(n_elem_insertion, Tn_insertion, c="blue")

    # add namings
    plt.title('insertion Sort: T(n) vs (n)')
    plt.xlabel("number of elements")
    plt.ylabel("number of operations (le7)")

    # To show the plot
    plt.show()
    '''
    As appears from the graph,  T(n) vs (n) in insertion Sort is O(n^2) complexity.
    We see that the curve is aligned with what we learned about the performance of insertion sort. 
    '''

    # step-4
    # plot time to perform the algorithm against number of elements

    time_insertion = [diff_insertion_10, diff_insertion_50, diff_insertion_100,
                      diff_insertion_500, diff_insertion_1000, diff_insertion_5000]

    # plot the values
    plt.scatter(n_elem_insertion, time_insertion, c="green")

    # add namings
    plt.title('insertion Sort: Time vs (n)')
    plt.xlabel("number of elements")
    plt.ylabel("number of operations (milliseconds)")

    # To show the plot
    plt.show()

    '''As with the graph in step 3, we can see a quadratic O(n²) time complexity.
    We see that the curve is aligned with what we learned about the performance of insertion sort. 
    '''

    print("*****************************************************************************************************************")

    print("~~~MERGE SORT CALCULATIONS~~~")

    # step-1
    # creating a random list of 100 elements
    random_100_merge = [random.randint(0, 300) for val in range(list_100)]
    print(f'list before sorting: {random_100_merge}\n')

    # test the algorithm
    merge_sort(random_100_merge)
    print(
        f'list after applying merge_sort on random 100 numbers: {random_100_merge}\n')

    # step-2 : add lines of code...added in the above function
    # test T(n) calculation

    # 1. Best case scenario - values already sorted
    random_50_merge = [random.randint(0, 300) for val in range(list_50)]
    random_50_merge.sort()
    print(random_50_merge)
    print(
        f'steps needed for sorting Best Case: {merge_sort(random_50_merge)}\n')
    '''Best case T(n) is O(n*log(n, 2)) - number of values times log base 2 of number of values
    In the above example - 50*log(50,2) = 282
    Which aligns with whaat we learned dabout merge sort algorithm
    '''

    # 2. Worst case scenario - values in reversed order (descending)
    random_50_merge.sort(reverse=True)
    print(random_50_merge)
    print(
        f'steps needed for sorting Worst Case: {merge_sort(random_50_merge)}\n')
    '''Best case T(n) is O(n*log(n, 2)) - number of values times log base 2 of number of values
    In the above example - 50*log(50,2) = 282
    Which aligns with what we learned about merge sort algorithm
     '''

    # 3. Average case scenario - for the average case about half of the values need to be sorted
    # I will create a random list of 50 elements to test
    random_50_average_merge = [random.randint(
        0, 300) for val in range(list_50)]
    print(random_50_average_merge)
    print(
        f'steps needed for sorting Average Case: {merge_sort(random_50_average_merge)}\n')
    '''Best case T(n) is O(n*log(n, 2)) - number of values times log base 2 of number of values
    In the above example - 50*log(50,2) = 282
    Which aligns with what we learned about merge sort algorithm
     '''

    # step-3
    # plot T(n) vs n

    # x-axis: number of elements
    # y-axis: T(n) calculation

    # creating lists for worst cases
    ran10_merge = [random.randint(0, 1000000) for val in range(size10)]
    ran10_merge.sort(reverse=True)
    # print(ran10_merge) # - testing - prints a random list in range 0-1M reversed order
    # print(merge_sort(ran10_merge))# - testing - returns T(n) in this case result: 58

    ran50_merge = [random.randint(0, 1000000) for val in range(size50)]
    ran50_merge.sort(reverse=True)

    ran100_merge = [random.randint(0, 1000000) for val in range(size100)]
    ran100_merge.sort(reverse=True)

    ran500_merge = [random.randint(0, 1000000) for val in range(size500)]
    ran500_merge.sort(reverse=True)

    ran1000_merge = [random.randint(0, 1000000) for val in range(size1000)]
    ran1000_merge.sort(reverse=True)

    ran5000_merge = [random.randint(0, 1000000) for val in range(size5000)]
    ran5000_merge.sort(reverse=True)
    # print(merge_sort(ran5000_merge)) #- result: 96624 - A LOT lOWER COMPARED TO SIMPLE SORTS!

    # sort the arrays, measure number of operations (for step3) and time (for step4)
    # convert the time to milliseconds
    time_start_merge_10 = round(time.time()*1000)
    merge_sorted10 = merge_sort(ran10_merge)
    time_end_merge_10 = round(time.time()*1000)
    diff_merge_10 = time_end_merge_10 - time_start_merge_10

    time_start_merge_50 = round(time.time()*1000)
    merge_sorted50 = merge_sort(ran50_merge)
    time_end_merge_50 = round(time.time()*1000)
    diff_merge_50 = time_end_merge_50 - time_start_merge_50

    time_start_merge_100 = round(time.time()*1000)
    merge_sorted100 = merge_sort(ran100_merge)
    time_end_merge_100 = round(time.time()*1000)
    diff_merge_100 = time_end_merge_100 - time_start_merge_100

    time_start_merge_500 = round(time.time()*1000)
    merge_sorted500 = merge_sort(ran500_merge)
    time_end_merge_500 = round(time.time()*1000)
    diff_merge_500 = time_end_merge_500 - time_start_merge_500

    time_start_merge_1000 = round(time.time()*1000)
    merge_sorted1000 = merge_sort(ran1000_merge)
    time_end_merge_1000 = round(time.time()*1000)
    diff_merge_1000 = time_end_merge_1000 - time_start_merge_1000
    # print(diff_merge_1000) # result - 4 ms A LOT lOWER COMPARED TO SIMPLE SORTS!

    time_start_merge_5000 = round(time.time()*1000)
    merge_sorted5000 = merge_sort(ran5000_merge)
    time_end_merge_5000 = round(time.time()*1000)
    diff_merge_5000 = time_end_merge_5000 - time_start_merge_5000
    # print(diff_merge_5000) # result - 25 ms A LOT lOWER COMPARED TO SIMPLE SORTS!

    # create X and Y values for the scatter plot
    n_elem_merge = [10, 50, 100, 500, 1000, 5000]
    Tn_merge = [merge_sorted10, merge_sorted50, merge_sorted100,
                merge_sorted500, merge_sorted1000, merge_sorted5000]

    # plot the values
    plt.scatter(n_elem_merge, Tn_merge, c="blue")

    # add namings
    plt.title('merge Sort: T(n) vs (n)')
    plt.xlabel("number of elements")
    # note numbers are NOT exponents - in the contrary to the simple sorts
    plt.ylabel("number of operations -note the exponent is 10^0")

    # To show the plot
    plt.show()

    # We have to adjust Y axis scale to the same as in simple sorts so we can see the comparison
    ax = plt.axes()
    ax.scatter(n_elem_merge, Tn_merge, c="blue")
    ax.set_title('merge Sort: T(n) vs (n) -adjusted scale')
    ax.set_xlabel("number of elements")
    ax.set_ylim(0, 10000000)
    ax.set_ylabel("number of operations -scale adjusted")
    plt.show()

    '''
    As appears from the graph,  T(n) vs (n) in Merge Sort is O(n*log(n,2)) log base2- complexity.
    We see that the curve is aligned with what we learned about the performance of merge sort. 
    And is a lot more favorable (less operations) compared to simple sorts!
    '''

    # step-4
    # plot time to perform the algorithm against number of elements

    time_merge = [diff_merge_10, diff_merge_50, diff_merge_100,
                  diff_merge_500, diff_merge_1000, diff_merge_5000]

    # plot the values
    plt.scatter(n_elem_merge, time_merge, c="green")

    # add namings
    plt.title('merge Sort: Time vs (n)')
    plt.xlabel("number of elements")
    plt.ylabel("number of operations (milliseconds)")

    # To show the plot
    plt.show()

    # We have to adjust Y axis scale to the same as in simple sorts so we can see the comparison
    ax = plt.axes()
    ax.scatter(n_elem_merge, time_merge, c="green")
    ax.set_title('merge Sort: T(n) vs (n) -adjusted scale')
    ax.set_xlabel("number of elements")
    ax.set_ylim(0, 3500)
    ax.set_ylabel("number of operations -scale adjusted")
    plt.show()

    '''As with the graph in step 3, we can see O(n*log(n,2)) log base2- complexity.
    We see that the curve is aligned with what we learned about the performance of merge sort.
    And is a lot faster compared to simple sorts!
    '''

    print("*****************************************************************************************************************")

    print("~~~QUICK SORT CALCULATIONS~~~")

    # step-1
    # creating a random list of 100 elements
    random_100_quick = [random.randint(0, 300) for val in range(list_100)]
    print(f'list before sorting: {random_100_quick}\n')

    # test the algorithm
    quick_sort(random_100_quick)
    print(
        f'list after applying quick_sort on random 100 numbers: {random_100_quick}\n')

    # step-2 : add lines of code...added in the above function
    # test T(n) calculation

    '''The best and worst cases would depend here on the pivot choice, 
    which is randomly selected, pre-sorting the values ascending/descending yelds similar results'''

    # CASE-1 -TESTING with n= 200 which is greater than a THRESHOLD

    print("n>Threshold")
    # 1. Best case scenario - values already sorted
    random_200_quick = [random.randint(0, 300) for val in range(200)]
    random_200_quick.sort()
    print(random_200_quick)
    print(
        f'steps needed for sorting Best Case: {quick_sort(random_200_quick)}\n')  # RESULT -> 2133 ~=200*log(200,2)

    # 2. Worst case scenario - values in reversed order (descending)
    random_200_quick.sort(reverse=True)
    print(random_200_quick)
    print(
        f'steps needed for sorting Worst Case: {quick_sort(random_200_quick)}\n')

    # 3. Average case scenario - for the average case about half of the values need to be sorted
    # I will create a random list of 200 elements to test
    random_200_average_quick = [random.randint(0, 300) for val in range(200)]
    print(random_200_average_quick)
    print(
        f'steps needed for sorting Average Case: {quick_sort(random_200_average_quick)}\n')

    print("n<Threshold")
    # CASE-2 -TESTING with n= 20 which is less than a THRESHOLD - whoild do the insertion sort
    random_20_quick = [random.randint(0, 300) for val in range(20)]
    random_20_quick.sort()
    print(random_20_quick)
    print(
        f'steps needed for sorting Best Case: {quick_sort(random_20_quick)}\n')  # RESULT -

    # 2. Worst case scenario - values in reversed order (descending)
    random_20_quick.sort(reverse=True)
    print(random_20_quick)
    print(
        f'steps needed for sorting Worst Case: {quick_sort(random_20_quick)}\n')

    # 3. Average case scenario - for the average case about half of the values need to be sorted
    # I will create a random list of 20 elements to test
    random_20_average_quick = [random.randint(0, 300) for val in range(20)]
    print(random_20_average_quick)
    print(
        f'steps needed for sorting Average Case: {quick_sort(random_20_average_quick)}\n')  # RESULT -> 405 ~=20*20

    '''CONCLUSION - If number of elements in less or equals to THRESHOLD, we get the simple sort behavior O(n^2)-WORST CASE
    O(n^2) average case O(n) best case
    However, if number of elements is greater than the THRESHOLD, we get O(n*log(n,2)) behavior in best and average cases
    and O(n^2) behavior in worst case - we cannot mimic the worst case since it occurs randomly, depending on the pivot selection.
    If the pivot selected every time at the edges of the array - we will get the worst case sencario.  
    '''
    # let's see what happens to an array of identical 100 elements
    arr_mimic_worst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    print("sorting array with identical 100 elements -> pivot will always be at the edge (test if we get a quadratic behavior)")
    # print(quick_sort(arr_mimic_worst)) # RESULT-> 18024 which is ~= 10*10
    '''so here the pivot was always at the edge case, since all values are equal and thus was no other choice for the pivot!
    We can see that in this case we indeed get O(n^2)'''

    # step-3
    # plot T(n) vs n

    # since we already know how n^2 behavior looks like,
    # I will plot here the average case of quick_sort, which is supposed to be n*log(n,2)
    # We will test if this is indeed the case
    # n>>THRESHOLD
    # values- ordered randomly (not reversed as in previous demonstrations)

    # x-axis: number of elements
    # y-axis: T(n) calculation

    # creating lists for worst cases

    ran100_quick = [random.randint(0, 1000000) for val in range(size100)]
    ran100_quick.sort()

    ran200_quick = [random.randint(0, 1000000) for val in range(200)]
    ran200_quick.sort()

    ran500_quick = [random.randint(0, 1000000) for val in range(500)]
    ran500_quick.sort()

    ran700_quick = [random.randint(0, 1000000) for val in range(700)]
    ran700_quick.sort()

    ran1000_quick = [random.randint(0, 1000000) for val in range(1000)]
    ran1000_quick.sort()

    ran5000_quick = [random.randint(0, 1000000) for val in range(5000)]
    ran5000_quick.sort(reverse=True)
    # - result: 228514 - A LOT lOWER COMPARED TO SIMPLE SORTS (by factor of 100)!
    print(quick_sort(ran5000_quick))

    # sort the arrays, measure number of operations (for step3) and time (for step4)
    # convert the time to milliseconds
    time_start_quick_100 = round(time.time()*1000)
    quick_sorted100 = quick_sort(ran100_quick)
    time_end_quick_100 = round(time.time()*1000)
    diff_quick_100 = time_end_quick_100 - time_start_quick_100

    time_start_quick_200 = round(time.time()*1000)
    quick_sorted200 = quick_sort(ran200_quick)
    time_end_quick_200 = round(time.time()*1000)
    diff_quick_200 = time_end_quick_200 - time_start_quick_200

    time_start_quick_500 = round(time.time()*1000)
    quick_sorted500 = quick_sort(ran500_quick)
    time_end_quick_500 = round(time.time()*1000)
    diff_quick_500 = time_end_quick_500 - time_start_quick_500

    time_start_quick_700 = round(time.time()*1000)
    quick_sorted700 = quick_sort(ran700_quick)
    time_end_quick_700 = round(time.time()*1000)
    diff_quick_700 = time_end_quick_700 - time_start_quick_700

    time_start_quick_1000 = round(time.time()*1000)
    quick_sorted1000 = quick_sort(ran1000_quick)
    time_end_quick_1000 = round(time.time()*1000)
    diff_quick_1000 = time_end_quick_1000 - time_start_quick_1000
    # print(diff_quick_1000) # result - 1 ms A LOT lOWER COMPARED TO SIMPLE SORTS!

    time_start_quick_5000 = round(time.time()*1000)
    quick_sorted5000 = quick_sort(ran5000_quick)
    time_end_quick_5000 = round(time.time()*1000)
    diff_quick_5000 = time_end_quick_5000 - time_start_quick_5000
    # print(diff_quick_5000) # result - 11 ms A LOT lOWER COMPARED TO SIMPLE SORTS!

    ##

    # create X and Y values for the scatter plot
    n_elem_quick = [100, 200, 500, 700, 1000, 5000]
    Tn_quick = [quick_sorted100, quick_sorted200, quick_sorted500,
                quick_sorted700, quick_sorted1000, quick_sorted5000]

    # plot the values
    plt.scatter(n_elem_quick, Tn_quick, c="blue")

    # add namings
    plt.title('quick Sort: T(n) vs (n)')
    plt.xlabel("number of elements")
    # note numbers are NOT exponents - in the contrary to the simple sorts
    plt.ylabel("number of operations -note the exponent is 10^0")

    # To show the plot
    plt.show()

    # We have to adjust Y axis scale to the same as in simple sorts so we can see the comparison
    ax = plt.axes()
    ax.scatter(n_elem_quick, Tn_quick, c="blue")
    ax.set_title('quick Sort: T(n) vs (n) -adjusted scale')
    ax.set_xlabel("number of elements")
    ax.set_ylim(0, 10000000)
    ax.set_ylabel("number of operations -scale adjusted")
    plt.show()

    '''
    As appears from the graph,  T(n) vs (n) in quick Sort (AVERAGE CASE) is O(n*log(n,2)) log base2- complexity.
    We see that the curve is aligned with what we learned about the performance of quick sort. 
    And is a lot more favorable (less operations) compared to simple sorts! (in AVERAGE/BEST CASEs)
    '''

    # step-4
    # plot time to perform the algorithm against number of elements

    time_quick = [diff_quick_100, diff_quick_200, diff_quick_500,
                  diff_quick_700, diff_quick_1000, diff_quick_5000]

    # plot the values
    plt.scatter(n_elem_quick, time_quick, c="green")

    # add namings
    plt.title('quick Sort: Time vs (n)')
    plt.xlabel("number of elements")
    plt.ylabel("number of operations (milliseconds)")

    # To show the plot
    plt.show()

    # We have to adjust Y axis scale to the same as in simple sorts so we can see the comparison
    ax = plt.axes()
    ax.scatter(n_elem_quick, time_quick, c="green")
    ax.set_title('quick Sort: T(n) vs (n) -adjusted scale')
    ax.set_xlabel("number of elements")
    ax.set_ylim(0, 3500)
    ax.set_ylabel("number of operations -scale adjusted")
    plt.show()

    '''As with the graph in step 3, we can see O(n*log(n,2)) log base2- complexity.
    We see that the curve is aligned with what we learned about the performance of quick sort.
    And is a lot faster compared to simple sorts! (in AVERAGE/BEST CASEs)
    '''

    print("*****************************************************************************************************************")
    # hope you enjoyed my analysis of various sorting algorithms
    print("~~~THE END~~~")


# calling main
if __name__ == "__main__":
    main()


# In[ ]:
