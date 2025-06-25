mylist2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

summed = 0
for i in range(len(mylist2d)):
    summed += mylist2d[i][i]

print("Sum of primary diagonal:", summed)
