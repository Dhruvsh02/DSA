# minimum window substring

# brute force approach using loops and map time complexity O(n^2)
def minWindow(s: str, t: str) -> str:
    n = len(s)
    m = len(t)
    min_len = 10**9
    s_index = -1
    for i in range(n):
        count = 0
        mpp = [0]*256
        for j in range(m):
            mpp[ord(t[j])] += 1
        for j in range(i,n):
            if mpp[ord(s[j])] > 0:
                count += 1
            mpp[ord(s[j])] -= 1
            if j-i+1 < min_len and count == m:
                min_len = j-i+1
                s_index = i
                break
    return s[s_index:s_index+min_len]

# test cases
print(minWindow("ADOBECODEBANC","ABC"))


# optimal approach using sliding window and map time complexity O(3n)

def optimal_minwindow(s: str, t: str) -> str:
    n = len(s)
    m = len(t)
    l = 0
    r = 0
    min_len = 10**9
    count = 0
    s_index = -1
    mpp = [0]*256
    for i in range(m):
        mpp[ord(t[i])] += 1
    while r< n:
        if mpp[ord(s[r])] > 0:
            count += 1
        mpp[ord(s[r])] -= 1
        while count == m:
            if r-l+1 < min_len:
                min_len = r-l+1
                s_index = l
            mpp[ord(s[l])] += 1
            if mpp[ord(s[l])] > 0:
                count -= 1
            l += 1
        r += 1 
    return s[s_index:s_index+min_len] if s_index != -1 else ""

# test cases
print(optimal_minwindow("ADOBECODEBANC","ABC"))