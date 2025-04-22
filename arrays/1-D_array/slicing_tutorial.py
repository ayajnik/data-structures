a = [1,2,3,4,5]
# for i in range(0,3+1):
#     print(a[i])

# [1:] --> this will give all the elements stating from index 1 and not the first element
# [:] --> returns all the elements
# [1:2] --> will return element at index 1 but not the element at second index because it always follows starting index to ending index -1

## we can also update the element in a list through slicking. Look at the example down below:

a[0:2] = ['x','y']
print(a)

print('-------------------------------x-----------------------------------')

# .pop() deletes the element from a list. If we provide the index then it will delete the element from that index only. Otherwise it will delete the last element only.

a.pop()
print(a)

print('-------------------------------x-----------------------------------')

a.pop(0)
print(a)

print('-------------------------------x-----------------------------------')

## if we want to remove the elemnts from a particular index, then we will prvide the index range and add del as prefix.

del a[0:2]
print(a)

print('-------------------------------x-----------------------------------')

## if we use .remove() method then it will just remove the element proided in the paramter of this method

a = a.remove(4)
if a == None:
    print("No elements left")
else:
    print(a)

print('-------------------------------x-----------------------------------')
