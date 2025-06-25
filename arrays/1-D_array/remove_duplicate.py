my_list = [1, 1, 2, 2, 3, 4, 5]

unique_list = []
seen = set()

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
    else:
        print(i,'already there so skipping and moving to the next one.')

print(unique_list)
print('\n')
print('Total number of elements in the list after removing the duplicates are',len(unique_list),'as compared to the original list which had',len(my_list),'elements')
        