# z- funncation algorithm / pattern searching : Given two strings, one is a text string, text, and the other is a pattern string, pattern. Print the indexes of all occurrences of the pattern string in the text string using the Z function algorithm. Use 0-based indexing while returning the indices.
# brute force approach 
def computeZarray(s):
    n = len(s)
    z = [0] * n 
    for i in range(1,n):
        while i + z[i] < n and s[i+ z[i]] == s[z[i]]:
            z[i] += 1
    return z 

def search(pattern,text):
    n = len(text) 
    m = len(pattern)
    s = pattern + '$' + text

    z = computeZarray(s)

    ans = []
    for i in range(m+1,len(s)):
        if z[i] == m:
            ans.append(i-(m+1))
    return ans 

def main():
    text = 'xyzsdncxyz'
    pattern = 'xyz'
    result = search(pattern,text)
    print(f"occurance of pattern in text : {result}")

if __name__=="__main__":
    main()


# optimal approach 

def computeZ(s):
    n = len(s)
    z = [0] * n
    left , right = 0 , 0 
    for i in range(1,n):
        if i > right :
            while i+z[i] < n and s[i+z[i]] == s[z[i]]:
                z[i] += 1
        else:
            if i+z[i-left] <= right:
                z[i] = z[i-left]
            else:
                z[i] = right-i+1
                while i+z[i] < n and s[i+z[i]] == s[z[i]] :
                    z[i] += 1
        left,right = i,i+z[i]-1
    return z 
def search(pattern,text):
    n = len(text) 
    m = len(pattern)
    s = pattern + '$' + text

    z = computeZ(s)

    ans = []
    for i in range(m+1,len(s)):
        if z[i] == m:
            ans.append(i-(m+1))
    return ans 

def main():
    text = 'xyzsdncxyzdjhcxyz'
    pattern = 'xyz'
    result = search(pattern,text)
    print(f"occurance of pattern in text : {result}")

if __name__=="__main__":
    main()

