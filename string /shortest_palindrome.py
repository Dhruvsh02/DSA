# shortest palindrome using LPS 

def compute(s):
    n = len(s)
    lps = [0] * n 
    i,j = 1,0

    while i < n :
        if s[i] == s[j]:
            lps[i] = j+1
            j+=1
            i+=1
        else:
            while j > 0 and s[i] != s[j]:
                j = lps[j-1]
            if s[i] == s[j] :
                lps[i] = j+1
                j+=1
            i+=1
    return lps 

def palindrome(s):
    rev_s = s[::-1]
    combined_s = s + '$' + rev_s
    lps = compute(combined_s)
    ans = len(s) - lps[-1]
    add = rev_s[:ans]

    return add + s

def main():
    s = 'adam'
    result = palindrome(s)
    print(f"shorted palindrome of string is:{result}")

if __name__=="__main__":
    main()



# leetcode 214

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        combine_s = s + '$' + rev_s
        n = len(combine_s)
        lps = [0]*n
        i,j = 1,0
        while i < n:
            if combine_s[i]==combine_s[j]:
                lps[i] = j+1
                j+=1
                i+=1
            else:
                while j > 0 and combine_s[i] != combine_s[j]:
                    j = lps[j-1]
                if combine_s[i] == combine_s[j]:
                    lps[i] = j+1
                    j+=1
                i+=1
        to_add = rev_s[:len(s) - lps[-1]]
        return to_add + s 

        