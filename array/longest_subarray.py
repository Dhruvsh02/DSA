# longest subarry with sum equal to its length (brute force approach)

def longest_subarray(arr,k):
    n = len(arr)
    max_length = 0 
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == k:   # sum of subarray is equal to its length
                max_length = max(max_length, j-i+1)
    return max_length

def main():
    arr = [1,2,3,4,3,1,1,2,3,5]
    k = 3
    result = longest_subarray(arr,k)
    print("The length of the longest subarray with sum",k,"is", result)
if __name__ == "__main__":
    main()


# using hashing map 

def longest_subarray(arr,k):
    pre_sum_map = {}
    n = len(arr)
    curr_sum = 0
    max_length = 0

    for i in range(n):
        curr_sum += arr[i]  # current sum of the array

        if curr_sum ==k:
            max_length = i+1     # if the sum is equal to k then length is i+1
        # if curr_sum - k is already in the map, it means we have found a subarray with sum k

        if (curr_sum - k) in pre_sum_map:    # if curr_sum - k is in the map
            length = i - pre_sum_map[curr_sum - k]   # length of the subarray
            max_length = max(max_length, length)

        if curr_sum not in pre_sum_map:
            pre_sum_map[curr_sum] = i     # store the index of the current sum
    # if the current sum is not in the map, store it with its index
    return max_length

def main():
    arr = [1,2,3,1,1,1,4]
    k = 6
    result = longest_subarray(arr,k)
    print("length of longest subarry with sum",k,"is",result)
if __name__ == "__main__":
    main()


# optimal approach using 2 pointers 

def longest_subarray(arr,k):
    left = 0
    right = 0 
    max_len = 0
    curr_sum = arr[0]
    n = len(arr)
    while right < n:
        while curr_sum > k and left <= right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == k:
            max_len = max(max_len, right - left + 1)
        right += 1
        if right < n :
            curr_sum += arr[right]
    return max_len

def main():
    arr = [1,2,3,1,1,1,1,3,3]
    k = 6
    result = longest_subarray(arr,k)
    print("length of longest subarry with sum",k,"is",result)
if __name__ == "__main__":
    main()


