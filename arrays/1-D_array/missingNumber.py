## we need to create a method where we need to find the missing number from the array.

def missingNumber(arr,n):
    sum1 = n*(n+1)//2
    sum2 = sum(arr)

    difference = sum1 - sum2

    return difference

if __name__ == "__main__":
    print(missingNumber([1, 2, 3, 4, 6], 6))