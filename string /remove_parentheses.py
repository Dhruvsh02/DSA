# remove outermost parentheses in a string 
# brute force approach 

def remove_parentheses(s):
    result = ""
    balance , start = 0 , 0 
    for i, ch in enumerate(s):
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            result += s[start+1:i]
            start = i+1
    return result 
def main():
    s = "(()())(())"
    result = remove_parentheses(s)
    print(result)
if __name__ == "__main__":
    main()

# optimal approach 

def remove_outer(s):
    result = []
    depth = 0
    for ch in s:
        if ch == '(':   # skip outermost
            if depth > 0:
                result.append(ch)
            depth+=1
        else:   # skip outermost 
            depth-=1
            if depth > 0:
                result.append(ch)
    return "".join(result)
def main():
    s = "(()())(())"
    result = remove_outer(s)
    print(result)
if __name__ == "__main__":
    main()