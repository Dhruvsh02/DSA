# longest happy prefix : Given a string s, return the longest happy prefix of s. A happy prefix is a string that is both a proper prefix and a proper suffix.

def computelps(s):
    n = len(s)
    lps = [0] *n 
    i,j = 1,0

    while i < n :
        if s[i] == s[j]:
            lps[i] = j+1
            j+=1
            i+=1
        else:
            while j>0 and s[i] != s[j]:
                j = lps[j-1]
            if s[i] == s[j]:
                lps[i] = j+1
                j+=1
            i+=1
    return lps 

def prefix(s):
    lps = computelps(s)
    return s[:lps[-1]]

def main():
    s = 'level'
    result = prefix(s)
    print(f"longest happy prefix is : {result}")

if __name__=="__main__":
    main()


# leetcode 1392

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
        