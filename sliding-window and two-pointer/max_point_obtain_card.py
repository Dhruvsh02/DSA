# maximum points you can obtain from cards

def max_score(nums, k):
    n = len(nums)
    lsum = 0 
    rsum = 0
    max_sum = 0
    for i in range(k):
        lsum = lsum + nums[i]
        max_sum = lsum
    right = n-1
    for i in range(k-1,-1,-1):
        lsum = lsum - nums[i]
        rsum = rsum + nums[right]
        right -= 1

        max_sum = max(max_sum,lsum+rsum)
    return max_sum

# test cases
print(max_score([6,2,3,4,7,2,1,7,1],4)) 