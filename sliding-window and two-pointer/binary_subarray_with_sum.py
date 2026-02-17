# binary subarray with sum / count subarray sum equal to k

def countSubarraySum(nums, k):
    if k < 0:
        return 0
    n = len(nums)
    l = 0
    r = 0
    count = 0
    summ = 0

    while r < n:
        summ += nums[r]
        while summ > k:
            summ -= nums[l]
            l += 1
        count = count + (r-l+1)
        r += 1
    return count
def binary_count(nums,k):
    return countSubarraySum(nums,k) - countSubarraySum(nums,k-1)

# test cases
print(binary_count([1,0,1,0,1],2))