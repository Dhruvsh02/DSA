# maximum nesting depth of parenthesis 

def max_depth(s):
    depth = 0 
    max_depth = 0
    for ch in s:
        if ch == '(':
            depth +=1
            max_depth = max(max_depth,depth)
        elif ch == ')':
            depth -=1
    return max_depth
def main():
    s = "(1+(2*3)+((8)/4))+1"
    result = max_depth(s)
    print(f"maximum nesting depth of parenthesis is : {result}")
if __name__=="__main__":
    main()

    