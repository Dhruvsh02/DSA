# subarrays with k different integers

# brute force approach time complexity O(n^2)

def subarraysWithKDistinct(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        mpp = {}
        for j in range(i,n):
            mpp[nums[j]] = mpp.get(nums[j],0) + 1
            if len(mpp) == k:
                count += 1
            elif len(mpp) > k:
                break
    return count

# test cases
print(subarraysWithKDistinct([1,2,1,3,4],2))

# optimal approach using sliding window and map time complexity O(n)

def subarray(nums,k):
    l = 0
    r = 0
    n = len(nums)
    count = 0
    mpp = {}
    while r < n:
        mpp[nums[r]] = mpp.get(nums[r],0)+1
        while len(mpp) > k:
            mpp[nums[l]] -= 1
            if mpp[nums[l]] == 0:
                del mpp[nums[l]]
            l += 1
        count = count + (r-l+1)
        r += 1
    return count 
def subarraysWithKDistinct(nums, k):
    return subarray(nums,k) - subarray(nums,k-1)

# test cases
print(subarraysWithKDistinct([1,2,1,3,4],2))