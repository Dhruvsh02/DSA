# count number of nice subarray
# will use same approach as binary subarray and convery a odd number into 1 and even number into 0 and then count the number of subarray with sum equal to k

def countSubarraySum(nums, k):
    if k < 0:
        return 0
    n = len(nums)
    l = 0
    r = 0
    count = 0 
    s = 0
    while r< n:
        s += nums[r] % 2
        while s > k:
            s -= nums[l] % 2
            l += 1
        count = count + (r-l+1)
        r += 1
    return count
def countNiceSubarray(nums, k):
    return countSubarraySum(nums,k) - countSubarraySum(nums,k-1)

# test cases
print(countNiceSubarray([1,1,2,1,1],3))