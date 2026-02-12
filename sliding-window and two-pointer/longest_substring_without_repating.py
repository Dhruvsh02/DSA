# Longest Substring without repeating characters

# using loops and map 

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    max_len = 0
    for i in range(n):
        hash = [0] * 256
        for j in range(i,n):
            if hash[ord(s[j])] == 1:
                break
            length = j - i + 1
            max_len = max(max_len,length)
            hash[ord(s[j])] = 1
    return max_len

# test cases
print(lengthOfLongestSubstring("abcabcbb"))


# using sliding window and map

def optimal_lengthOfLongestSubstring(s: str) -> int:
    hash = [-1] * 256
    n = len(s)
    l = 0
    r = 0
    max_len = 0
    while r < n: 
        if hash[ord(s[r])] != -1:  # in the map 
            if hash[ord(s[r])] >= l:   # last index of character is >= l to avoid the repeating character
                l = hash[ord(s[r])] + 1
        length = r-l+1
        max_len = max(max_len,length)
        hash[ord(s[r])] = r
        r+=1

    return max_len

# test cases
print(optimal_lengthOfLongestSubstring("abcabcbb"))
