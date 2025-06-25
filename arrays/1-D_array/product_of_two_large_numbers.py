nums = [3,5,7,8,9,10]

## we are assuming the value assigned to max1 and max2 have higher value
max1 = 0
max2 = 0

for numbers in nums:
    ## we are checking that the current number in the iteration is bigger than the value of max1
    if numbers > max1:
        ## assign max2 the max1's previous bigger value
        max2 = max1
        
        ## if they are bigger than the current value, then assign max1 the value of numbers
        max1 = numbers
        
    elif numbers > max2:
        max2 = numbers

product = max1 * max2
print(product)