nums = [-4,-1,0,3,10]

for i,j in enumerate(nums):
    nums[i] = nums[i] * nums[i]

nums.sort() 
print(nums)