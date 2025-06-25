original = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

for i in range(len(original)):
    print('First iteration',i)
    for j in range(i,len(original)):
        print('Second iteration',j)
        original[i][j], original[j][i] = original[j][i], original[i][j]
        print('\n')

for row in original:
    row.reverse()

print(original)