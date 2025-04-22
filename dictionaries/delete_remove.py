a = {'name': 'Ayush', 'age': 30, 'Location': 'New Delhi/New York'}

## deleting a key

del a['name']
print(a)

## removing a specific key from the dictionary

a.pop('Location')
print(a)

## remove last element from the dictionary

a.popitem()
print(a)

## then we can use .clear() to remove all the elements from the dictionary