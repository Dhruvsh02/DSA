# rotate string : check whether one string in a rotation of another 
# brute force method 
def rotate(s,goal):
    n = len(s)
    if len(s) != len(goal):
        return False
    for i in range(n):
        rotated = s[i:] + s[:i]
        if rotated == goal:
            return True
    return False

def main():
    s = 'abcde'
    goal = 'cdeab'
    result = rotate(s,goal)
    print(result)

if __name__ == "__main__":
    main()

# optiaml approach 

def rotate_string(s,goal):
    if len(s) != len(goal):
        return False
    double_s = s + s 
    if goal in double_s:
        return True
    return False

def main():
    s = 'abcde'
    goal = 'cdeab'
    result = rotate_string(s,goal)
    print(result)