nums = [1,2,3,4,5,6,7,8,9,10]

for idx, number in enumerate(nums):
    if idx == 0:
        first = number
        print("First number in the list:", first)
    elif idx == len(nums) - 1:
        last = number
        print("Last number in the list:", last)

nums.remove(first)
nums.remove(last)

print(nums)
