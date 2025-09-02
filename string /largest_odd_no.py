# largest odd number in string 

def largest_odd(s):
    n = len(s)
    ind = -1
    i=0
    for i in range(n-1,-1,-1):
        if (int(s[i])%2)== 1:
            ind = i 
            break 
    i = 0
    while i <= ind and s[i] == '0' :
        i +=1
    return s[i:ind+1]
def main():
    s = "002349812"
    result = largest_odd(s)
    print(f"largest odd number in string is : {result}")
if __name__=="__main__":
    main()

def largest(s):
    for i in range(len(s)-1,-1,-1):
        if (int(s[i])%2)== 1:
            result = s[:i+1]
            return result.lstrip("0")
    return ""