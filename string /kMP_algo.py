# KMP algorithm or LPS array :Given two strings, one is a text string, text, and the other is a pattern string, pattern. Find and print the indices of all the occurrences of the pattern string within the text string. Use 0-based indexing for the indices, and ensure that the indices are in ascending order. If the pattern does not occur in the text, return an empty list.

# brute force approach 

def computekmp(s):
    n = len(s)
    lps = [0] * n 
    for i in range(1,n):
        for length in range(1,i):
            if s[:length] == s[i-length+1:i+1]:
                lps[i] = length 
    return lps 

def search(pattern,text):
    n = len(text)
    m = len(pattern)
    ans = []
    s = pattern + '$' + text 
    lps = computekmp(s)
    for i in range(m+1,len(s)):
        if lps[i] == m:
            ans.append(i-2*m)
    return ans

def main():
    text = "ababcababcabc"
    pattern = "abc"
    result = search(pattern,text)
    print(f"pattern found at indices: {result}")
if __name__ == "__main__":
    main()


# optimal approach  

def computekmp(s):
    n = len(s)
    lps = [0] * n 
    i,j = 1,0
    while i < n:
        if s[i] == s[j]:
            lps[i] = j+1
            j+=1
            i+=1
        else:
            while j>0 and s[i]!=s[j]:
                j = lps[j-1]
            if s[i] == s[j]:
                lps[i] = j+1 
                j+=1
            i+=1
    return lps 

def search(pattern,text):
    n = len(text)
    m = len(pattern)
    ans = []
    s = pattern + '$' + text
    lps = computekmp(s)
    for i in range(m+1,len(s)):
        if lps[i] == m:
            ans.append(i-2*m)
    return ans 

def main():
    text = "ababcababcabcsdvhjfiubabc"
    pattern = "abc"
    result = search(pattern,text)
    print(f"pattern found at indices: {result}")
if __name__ == "__main__":
    main()
