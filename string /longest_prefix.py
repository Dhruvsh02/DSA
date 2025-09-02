# longest common prefix 
# best approach 

def longestcommon(strs):
     if not strs:
         return ""
    
     prefix = strs[0]
     for s in strs[1:]:
         while not s.startswith(prefix):
             prefix = prefix[:-1]
             if not prefix:
                 return ""
     return prefix

def main():
    strs = ["flower", "flow", "flight"]
    result = longestcommon(strs)
    print("longest common prefix:", result)

if __name__ == "__main__":
    main()



# lps approach but not working 
# storing in the lps array     
def build_lps(pattern):
    n = len(pattern)
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def longestcommon(s):
    lps = build_lps(s)
    return s[:lps[-1]]

def main():
    s = ["flower", "flow", "flight"]
    result = longestcommon(s)
    print("longest common prefix:", result)


if __name__ == "__main__":
    main()

