a = {'name': 'Ayush', 'age': 30, 'Location': 'New Delhi/New York'}

def searching(val,myDict:dict):
    for i in myDict:
        if myDict[i] == val:
            print(i, myDict[i])
            
print(searching(30,a)) 