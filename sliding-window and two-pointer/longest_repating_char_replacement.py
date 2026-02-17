# longest repeating character replacement 
# brute force approach using loops and map time complexity O(n^2)

def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    max_len = 0
    for i in range(n):
        mpp = [0]*26
        max_f = 0
        for j in range(i,n):
            mpp[ord(s[j]) - ord('A')] += 1
            max_f = max(max_f,mpp[ord(s[j]) - ord('A')])
            changes = (j-i+1) - max_f
            if changes <= k:
                max_len = max(max_len,j-i+1)
            else:
                break
    return max_len

# test cases 
print(characterReplacement("AABABBA",2))

# better approach using sliding window and map time complexity O(2n)

def better_characterReplacement(s: str, k: int) -> int:
    n = len(s)
    l = 0
    r = 0
    max_len = 0
    max_f = 0
    mpp = [0]*26
    while r < n:
        mpp[ord(s[r]) - ord("A")] += 1
        max_f = max(max_f,mpp[ord(s[r]) - ord("A")])
        while (r-l+1) - max_f > k:
            mpp[ord(s[l]) - ord("A")] -= 1
            max_f = 0
            for i in range(26):
                max_f = max(max_f,mpp[i])
            l += 1
        if (r-l+1) - max_f <= k:
            length = r-l+1
            max_len = max(length,max_len)
        r += 1
    return max_len

# test cases
print(better_characterReplacement("AABABBA",2))


# optimal approach using sliding window and map time complexity O(n)

def optimal_characterReplacement(s: str, k: int) -> int:
    l = 0 
    r = 0
    n = len(s)
    max_f = 0
    max_len = 0
    mpp = [0]*26
    while r<n:
        mpp[ord(s[r]) - ord("A")] += 1
        max_f = max(max_f,mpp[ord(s[r]) - ord("A")])
        if (r-l+1) - max_f > k:
            mpp[ord(s[l]) - ord("A")] -= 1
            l += 1
        if (r-l+1) - max_f <= k:
            length = r-l+1
            max_len = max(length,max_len)
        r += 1
    return max_len

# test cases
print(optimal_characterReplacement("AABABBA",2))