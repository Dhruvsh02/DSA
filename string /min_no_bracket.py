# minimum number of bracket reversals needed to make an expression balanced 

def min_reversals(s):
    n = len(s)
    if n%2 != 0:
        return -1
    
    open = 0
    close = 0
    for char in s:
        if char == '(':
            open +=1
        else:
            if open > 0:
                open -=1
            else:
                close +=1
    ans = (open // 2) + (open%2) + (close//2) + (close%2) 
    return ans 

def main():
    s = ')))(())((('
    result = min_reversals(s)
    print(f"minimum number of bracket reversals needed to make an expression balanced is : {result}")   
if __name__ == "__main__":
    main()


# for leetcode : 921

def min(s):
    open , close = 0,0
    for char in s:
        if char == '(':
            open +=1
        else:
            if open > 0:
                open -=1
            else:
                close +=1
    return close + open