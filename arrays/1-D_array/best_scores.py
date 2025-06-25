myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

max1 = 0
max2 = 0

for i in myList:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i

print('Best scpres in the class are',max1,max2)