## we can create a copy of a dictionary

a = {'name': 'Ayush', 'age': 30, 'Location': 'New Delhi/New York'}

b = a.copy()

print(a)
print(b)

## fromkeys: this method will help us create a dictionary: This initialized the dictionary with a single default value

newDict = {}.fromkeys([1,2,3,4],0)
print(newDict)

## get() --> this will be used for searching an element in the dictionary

print(b.get('name')) # this will return the value for the key that we are trying to search

## .itms() --> this will return the key and value in tuple format

for i in b.items():
    if 'name' in i:
        print(i)

## .keys() --> this will return keys in a dictionary

for i in b.keys():
    if 'name' in i:
        print(b[i])

##.popitem() --> remove the last key from the dictionary

removed_item = b.popitem()
print(removed_item)
print(b)

## .values()

for i in b.values():
    if i == 'Ayush':
        print(True)

## .update() --> if we want to append the values from one dictionary to another, then we can use the update method.

d = {'a':1}
b.update(d)
print(b)