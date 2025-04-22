from array import *

# 1. Create an array and traverse. 
print('Step 1')
my_array = array('i',[1,2,3,4,5])
for i in my_array:
    print(i)
print('-------------------------------x-----------------------------------')


# 2. Access individual elements through indexes

print("Step 2")
print(my_array[2])
print('-------------------------------x-----------------------------------')

# # 3. Append any value to the array using append() method

print("Step 3")
my_array.append(6)
print(my_array)
print('-------------------------------x-----------------------------------')


# # 4. Insert value in an array using insert() method
print("Step 4")
my_array.insert(2,11)
print(my_array)
print('-------------------------------x-----------------------------------')

# # 5. Extend python array using extend() method
## when we invoke the method extend(), then we are just appending a new list to an existing list

print("Step 5")
my_array1 = array('i',[20,21,22])
my_array.extend(my_array1)
print(my_array)
print('-------------------------------x-----------------------------------')

# # 6. Add items from list into array using fromlist() method: This will always append 
print("Step 6")
tempList = [10,11,12]
my_array.fromlist(tempList)
print(my_array)
print('-------------------------------x-----------------------------------')

# # 7. Remove any array element using remove() method: Let's say we have two elements with same value, then it will remove only one element which is coming the first time.
print("Step 7")
my_array.remove(11)
print(my_array)
print('-------------------------------x-----------------------------------')

# # 8. Remove last array element using pop() method
print("Step 8")
my_array.pop()
print(my_array)
print('-------------------------------x-----------------------------------')

# # 9. This will give us the index of the elements
print("Step 9")
print(my_array.index(21))
print('-------------------------------x-----------------------------------')

# # 10. Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)
print('-------------------------------x-----------------------------------')

# # 11. Get array buffer information through buffer_info() method
print("Step 11")
print(my_array.buffer_info())
print('-------------------------------x-----------------------------------')

# # 12. Check for number of occurrences of an element using count() method
print("Step 12")
my_array.append(11)
count_eleven = my_array.count(11)
print(count_eleven)
print('-------------------------------x-----------------------------------')

# # 13. Convert array to string using tostring() method
print("Step 13")
strTemp = my_array.tobytes()
print(strTemp)
ints = array('i')
ints.frombytes(strTemp)
print(ints)
print('-------------------------------x-----------------------------------')

# # 14. Convert array to a python list with same elements using tolist() method
print("Step 14")
print(my_array.tolist())
print('-------------------------------x-----------------------------------')

# # 16. Slice Elements from an array
print("Step 16")
print(my_array[1:4])
print('-------------------------------x-----------------------------------')





