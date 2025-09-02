# leetcode -28
# using z function algorithm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = needle+'$'+haystack 
        n = len(s)
        m = len(needle)
        z = [0] * n
        left,right = 0,0
        for i in range(1,n):
        #     while i+z[i] < n and s[i+z[i]] == s[z[i]]:
        #         z[i]+=1
        # for i in range(m+1,len(s)):
        #     if z[i] == m:
        #         return (i-(m+1))
            if i > right:
                while i+z[i] < n and s[i+z[i]] == s[z[i]]:
                    z[i]+=1
            else:
                if 1+z[i-left] <=right:
                    z[i] = z[i-left]
                else:
                    z[i] = right - i+1
                    while i+z[i]<n and s[i+z[i]] == s[z[i]]:
                        z[i]+=1
        for i in range(m+1,len(s)):
            if z[i] == m:
                return i-(m+1)
        
             
        return -1
    
# using kmp algorithm and lps array
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = haystack+'$'+needle
        n = len(s)
        m = len(needle)
        lps = [0]*n
        i,j = 1,0
        while i < n :
            if s[i] == s[j]:
                lps[i] = j+1
                j+=1
                i+=1
            else:
                while j > 0 and s[i] != s[j]:
                    j = lps[j-1]
                if s[i] == s[j]:
                    lps[i] = j+1
                    j+=1
                i+=1
        for i in range(m+1,n):
            if lps[i] == m:
                return i-2*m
        return -1

        