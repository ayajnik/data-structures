## find the subset of pairs of numbers which is equal to the sum of the target provided in the method as an argument

def twopairsum(arr, target):
    pairs = []
    # To avoid checking the same pair twice
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

if __name__ == "__main__":
    print(twopairsum([1, 2, 3, 2, 3, 4, 5, 6], 6))

#############################################################################


