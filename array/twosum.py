# two sum problem ( brute force approach )

def two_sum(arr, target):
    n = len(arr)
    for i in range(n):       
        for j in range(n):    # (i=1,n) will reduce the time complexity
            if i == j:     # then no need to check
                continue
            if arr[i]+arr[j] == target:
                return i,j
    return -1,-1  # if no such pair is found

def main():
    arr = [1,2,3,4,5]
    target = 6
    result = two_sum(arr, target)
    if result == (-1,-1):
        print("No such pair found")
    else:
        print("Pair found at indices:", result)
if __name__ == "__main__":
    main()



# better approach using hashing map

def two_sum(arr, target):
    num_map = {}
    n = len(arr)
    for i in range(n):
        complement = target-arr[i]
        if complement in num_map:    # if the complement is already in the map
            return num_map[complement], i   # return the indices of the two numbers
        num_map[arr[i]] = i   # store the index of the current number
    return -1,-1  # if no such pair is found

def main():
    arr = [1,2,3,4,5]
    target = 6
    result = two_sum(arr, target)
    if result == (-1,-1):
        print("No such pair found")
    else:
        print("Pair found at indices:", result)
if __name__ == "__main__":
    main()



# optimal approach using 2 pointers


def two_sum(arr, target):
    arr.sort()   # sort the array
    left = 0
    right = len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return left,right
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return -1,-1  # if no such pair is found

def main():
    arr = [1,2,3,4,5]
    target = 6
    result = two_sum(arr, target)
    if result == (-1,-1):
        print("No such pair found")
    else:
        print("Pair found at indices:", result)
if __name__ == "__main__":
    main()


