# def function1(value, number):								
# 	if (number == 0):							
# 		return 1						
# 	elif (number == 1):							
# 		return value						
# 	else:							
# 		return value * function1(value, number-1)						

# print (function1(2,1))
# print (function1(2,2))
# print (function1(2,3))
# print (function1(2,4))
# print (function1(2,5))

# # print (function1(2,0))
# print (function1(3,1))
# print (function1(3,2))
# print (function1(3,3))
# print (function1(3,4))
# print (function1(3,5))

# print (function1(4,2))
# print (function1(4,3))
# print (function1(4,4))
# print (function1(4,5))

def recursive_function2(mystring,a, b):  # hello (0, len(mystring)-1)
	if(a > b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

# print(function2('anna'))
# print(function2('mom'))
# print(function2('mams'))
# print(function2('palindrome'))
# print(function2('anna'))

def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result



print(function3(2,5))
print(function3(2,2))
print(function3(2,1))


print(function3(3,6))
print(function3(3,3))
print(function3(3,1))