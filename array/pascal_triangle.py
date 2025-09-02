# given row and column find our the element at that position in Pascal's Triangle

def n_c_r(n,r):
    result = 1
    for i in range(r):
        result = result * (n-i)
        result = result // (i + 1)
    return result

def main():
    n = 5  # row number
    r = 3 # column number
    result = n_c_r(n, r)
    print(f"The element at row {n} and column {r} in Pascal's Triangle is: {result}")
if __name__ == "__main__":
    main()


# print any Nth row of Pascal's Triangle

def nth_row_pascal_triangle(n):
    row = [1]  # First element is always 1
    ans = 1
    for i in range(1, n + 1):
        ans = ans * (n - i + 1) 
        ans = ans // i
        row.append(ans)
    return row

    
def main():
    n = 5  # row number
    result=nth_row_pascal_triangle(n)
    print(f"The {n}th row of Pascal's Triangle is: {result}")
if __name__ == "__main__":
    main()

# pascal triangle printing

def print_pascal_triangle(n):
    ans = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(n_c_r(i, j))
        ans.append(row)
    return ans
def main():
    n = 5  # number of rows
    result = print_pascal_triangle(n)
    print("Pascal's Triangle:")
    for row in result:
        print(row)
if __name__ == "__main__":
    main()