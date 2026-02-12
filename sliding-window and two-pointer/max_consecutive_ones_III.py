# max consecutive ones III 

# brute force approach time complexity O(n^2)

def longestOnes(nums, k):
    n = len(nums)
    max_len = 0
    for i in range(n):
        zeros = 0
        for j in range(i,n):
            if nums[j] == 0:
                zeros += 1
            if zeros <= k:
                length = j - i + 1
                max_len = max(length,max_len)
            else:
                break
    return max_len

# test cases
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))

# optimal approach using sliding window time complexity O(2n)

def better_longestOnes(nums, k):
    n = len(nums)
    l = 0
    r = 0 
    max_len = 0
    zeros = 0
    while r < n:
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        if zeros <= k:
            length = r-l+1
            max_len = max(length,max_len)
        r += 1
    return max_len

# test cases
print(better_longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))


# optimal approach using sliding window time complexity O(n)

def optimal_longestOnes(nums, k):
    n = len(nums)
    l = 0
    r = 0
    max_len = 0
    zero = 0
    while r < n:
        if nums[r] == 0:
            zero += 1
        if zero > k:
            if nums[l] == 0:
                zero -= 1
            l += 1
        if zero <= k:
            length = r-l+1
            max_len = max(length,max_len)
        r += 1
    return max_len

# test cases
print(optimal_longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))