

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# let "number" represent the value we are finding the total for
# let "total" represent function's output (answer)
# let T(n) represent number of operations needed to find the total

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTION-1

# python
def function1(number):
    total = 0  # 1

    for i in range(0, number):  # 1 for range, n loop iterations
        x = (i+1)              # 2n
        total += (x*x)  # 2n

    return total  # 1

# Math expression:
# 1+1+n+2n+2n+1 = 3+5n

# Final result:
# T(n) is O(n)


# TESTING
print(function1(1))  # 1
print(function1(2))  # 5
print(function1(3))  # 14


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTION-2

# python
def function2(number):
    # 3 operations for number replacement, 2 operations for additions, 3 multiplications, 1 division
    return ((number)*(number+1)*(2*number + 1))/6


# Math expression:
# 3+2+3+1 =9

# Final result:
# T(n) is O(1)


# TESTING
print(function2(1))  # 1
print(function2(2))  # 5
print(function2(3))  # 14
print(function2(4))  # 30


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTION-3
# Analyze the following with respect to the length of the list.

# python
def function3(list):
    # 1 for range, 1 for establishing length, n iterations (as per length of the list)
    for i in range(0, len(list)-1):
        # 1 for range, 1 for establishing length, n-1-i (i being the counter of the outer loop)
        for j in range(0, len(list)-1-i):
            if (list[j] > list[j+1]):  # n-1-i
                tmp = list[j]  # n-1-i
                list[j] = list[j+1]  # n-1-i
                list[j+1] = tmp  # n-1-i

# Math expression:
# (1+1+n)(1+5(n-1-i))= 2n*(5n-5i-4)= 10n^2-10ni-8n

# Final result:
# T(n) is O(n^2)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTION-4


# python
def function4(number):
    total = 1  # 1
    for i in range(1, number):  # 1 for range, n-1 loop iterations
        # (n-1)times incrementing, (n-1) times assigning to total
        total *= (i+1)
    return total  # 1

# Math expression:
# 1+1+n-1+2(n-1)+1 = 3n

# Final result:
# T(n) is O(n)


# TESTING
print(function4(0))  # 1
print(function4(1))  # 1
print(function4(2))  # 2
print(function4(3))  # 6
print(function4(4))  # 24
