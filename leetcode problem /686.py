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

 

