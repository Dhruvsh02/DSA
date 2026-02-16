# longest substring with at most k distinct characters

# brute force approach using loops and map time complexity O(n^2)
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    n = len(s)
    max_len = 0
    mpp = {}
    for i in range(n):
        mpp.clear()
        for j in range(i,n):
            mpp[s[j]] = mpp.get(s[j],0)+1
            if len(mpp) <= k:
                length = j-i+1
                max_len = max(length,max_len)
            else:
                break
    return max_len

# test cases
print(lengthOfLongestSubstringKDistinct("aaabbccd",2))

# better approach using sliding window and map time complexity O(2n)

def better_lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    n = len(s)
    l = 0
    r = 0
    max_len = 0
    hash_map = {}
    while r < n:
        hash_map[s[r]] = hash_map.get(s[r],0)+1
        if len(hash_map) > k:
            while len(hash_map) > k:
                hash_map[s[l]] -= 1
                if hash_map[s[l]] == 0:
                    del hash_map[s[l]]
                l += 1
        if len(hash_map) <= k:
            length = r-l+1
            max_len = max(length,max_len)
        r += 1
    return max_len

# test cases
print(better_lengthOfLongestSubstringKDistinct("aaabbccd",2))


# optimal approach using same sliding window and two pointer 

def optimal_distinct_character(s: str, k: int) -> int:
    n = len(s)
    l = 0
    r = 0
    max_len = 0
    mpp = {}
    while r < n:
        mpp[s[r]] = mpp.get(s[r],0)+1
        if len(mpp) > k:
            mpp[s[l]] -= 1
            if mpp[s[l]] == 0:
                del mpp[s[l]]
            l += 1
        if len(mpp) <= k:
            length = r-l+1
            max_len = max(length,max_len)
        r += 1
    return max_len

# test cases
print(optimal_distinct_character("aaabbccd",2))
