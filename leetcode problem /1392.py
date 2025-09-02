class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0]*n
        i,j = 1,0
        while i < n:
            if s[i] == s[j] :
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
        return s[:lps[-1]]
        