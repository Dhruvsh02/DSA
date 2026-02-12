# fruit and basket problem in which we have to find the longest subarray with at most 2 distinct characters

# brute force approach using loops and set time complexity O(n^2)

def totalFruit(fruits):
    n = len(fruits)
    max_len = 0
    for i in range(n):
        set_map = set()
        for j in range(i,n):
            set_map.add(fruits[j])
            if len(set_map) <= 2:
                max_len = max(max_len,j-i+1)
            else:
                break
    return max_len

# test cases
print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))


# optimal approach using sliding window and map time complexity O(2n)

def better_totalFruit(fruits):
    n = len(fruits)
    l = 0
    r = 0
    max_len = 0
    mp = {}
    while r < n:
        mp[fruits[r]] = mp.get(fruits[r],0) + 1
        if len(mp) > 2:
            while len(mp) > 2:
                mp[fruits[l]] -= 1
                if mp[fruits[l]] == 0:
                    del mp[fruits[l]]
                l += 1
        if len(mp) <= 2:
            length = r-l+1
            max_len = max(length,max_len)
        r += 1
    return max_len

# test cases
print(better_totalFruit([3,3,3,1,2,1,1,2,3,3,4]))


# optimal approach using sliding window and map time complexity O(n)

def optimal_totalFruit(fruits):
    n = len(fruits)
    l = 0
    r = 0
    max_len = 0
    mpp = {}

    while r < n:
        mpp[fruits[r]] = mpp.get(fruits[r],0) + 1
        if len(mpp) > 2:
            mpp[fruits[l]] -= 1
            if mpp[fruits[l]] == 0:
                del mpp[fruits[l]]
            l += 1
        if len(mpp) <= 2:
            length = r-l+1
            max_len = max(length,max_len)
        r += 1
    return max_len

# test cases
print(optimal_totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

