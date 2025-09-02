# rabin karp algorithm / repeated string match 
# brute force approach

def rabin_karp(text,pattern):
    n = len(text)
    m = len(pattern)
    ans = []
    if m > n:
        return -1
    for i in range(n-m+1):
        flag = True
        for j in range(m):
            if pattern[j] != text[i+j]:
                flag = False
                break
        if flag:
            ans.append(i)
    return ans 

def main():
    text = "ababcababcabc"
    pattern = "abc"
    result = rabin_karp(text,pattern)
    print(f"pattern found at indices: {result}")
if __name__ == "__main__":
    main()


# optimal approach

def rabin_karp_optimal(text,pattern):
    n = len(text)
    m = len(pattern)
    p = 7
    mod  = 10**9+9
    hash_pattern = 0
    hash_text = 0
    p_right = 1
    p_left = 1
    ans = []

    for i in range(m):
        hash_pattern = (hash_pattern + ((ord(pattern[i]) - ord('a') + 1 ) * p_right ) % mod ) % mod 
        hash_text = (hash_text + ((ord(text[i]) - ord('a') + 1)* p_right) % mod) % mod 
        p_right = (p_right * p) % mod 

    for i in range(m-n+1):

        if hash_pattern == hash_text :
            if text[i:i + n] == pattern:
                ans.append(i)

        if i < m-n:
            hash_text = (hash_text - ((ord(text[i]) - ord('a') + 1) * p_left ) % mod + mod) % mod 
            hash_pattern = (hash_pattern - ((ord(pattern[i]) - ord('a')) * p_left )% mod + mod ) % mod 
            hash_pattern = (hash_pattern * p ) % mod 

            p_left = (p_left * p ) % mod 
            p_right = (p_right * p ) % mod 

    return ans   

def main():
    text = "ababcababcabc"
    pattern = "abc"
    result = rabin_karp(text,pattern)
    print(f"pattern found at indices: {result}")
if __name__ == "__main__":
    main()



# leetcode 686
import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)
        repeats = math.ceil(m / n)
        base = 256
        mod = 10**9 + 9

        # hash of pattern b
        hash_b = 0
        for ch in b:
            hash_b = (hash_b * base + ord(ch)) % mod
        power = pow(base, m - 1, mod)

        # check repeats, repeats+1, repeats+2
        for k in [repeats, repeats + 1, repeats + 2]:
            text = a * k
            n_text = len(text)

            # rolling hash of first window
            hash_window = 0
            for i in range(m):
                hash_window = (hash_window * base + ord(text[i])) % mod

            if hash_window == hash_b and text[:m] == b:
                return k

            # slide window
            for i in range(m, n_text):
                hash_window = (hash_window - ord(text[i - m]) * power) % mod
                hash_window = (hash_window * base + ord(text[i])) % mod
                hash_window %= mod

                if hash_window == hash_b and text[i - m + 1:i + 1] == b:
                    return k

        return -1

 





class Solution:
    # Compute the Longest prefix suffix array for the combined string
    def computeLPS(self, s):
        n = len(s)  # size of string

        # To store the longest prefix suffix
        LPS = [0] * n

        i, j = 1, 0

        # Iterate on the string
        while i < n:
            # If the character matches
            if s[i] == s[j]:
                LPS[i] = j + 1
                i += 1
                j += 1

            # Otherwise
            else:
                # Trace back j pointer till it does not match
                while j > 0 and s[i] != s[j]:
                    j = LPS[j - 1]

                # If a match is found
                if s[i] == s[j]:
                    LPS[i] = j + 1
                    j += 1
                i += 1

        return LPS  # Return the computed LPS array

    '''
    Function to find the longest happy
    prefix of the given string
    '''
    def lps(self, s):
        LPS = self.computeLPS(s)
        return s[:LPS[-1]]


if __name__ == "__main__":
    s = "ababab"

    # Creating an instance of the solution class
    sol = Solution()

    '''
    Function call to find the longest
    happy prefix of the given string
    '''
    ans = sol.lps(s)

    print("The longest happy prefix of the given string is:", ans)



class Solution:
    # Compute the Longest prefix suffix array for the combined string
    def computeLPS(self, s):
        n = len(s)  # size of string

        # To store the longest prefix suffix
        LPS = [0] * n

        i, j = 1, 0

        # Iterate on the string
        while i < n:
            # If the character matches
            if s[i] == s[j]:
                LPS[i] = j + 1
                i += 1
                j += 1
            
            # Otherwise
            else:
                # Trace back j pointer till it does not match
                while j > 0 and s[i] != s[j]:
                    j = LPS[j - 1]
                
                # If a match is found
                if s[i] == s[j]:
                    LPS[i] = j + 1
                    j += 1
                
                i += 1
        
        return LPS  # Return the computed LPS array
    
    # Function to find the shortest palindrome by inserting
    # characters at the beginning of given string
    def shortestPalindrome(self, s):
        
        # To store the reverse string
        revs = s[::-1]
        
        # Forming the combined string
        str_combined = s + '$' + revs
        
        # Computing the LPS array
        lps = self.computeLPS(str_combined)
        
        # Calculating the answer
        ans = len(s) - lps[-1]
        
        # Finding the smallest string to be added in front of the given string
        to_add = revs[:ans]
        
        # Return the result
        return to_add + s


if __name__ == "__main__":
    s = "aacecaaa"
    
    # Creating an instance of the solution class
    sol = Solution()
    
    # Function call to find all indices of pattern in text
    ans = sol.shortestPalindrome(s)
    
    print(ans)

