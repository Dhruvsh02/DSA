# check if a given linked list is palindrome or not 

# brute force approach : using stack data structure

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def is_palindrome_ll(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        if temp.data != stack.pop():
            return False
        temp = temp.next
    return True

def main():
    arr = [1,2,3,2]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = current.next
    if is_palindrome_ll(head):
        print("Palindrome")
    else:
        print("Not a Palindrome")
if __name__ == "__main__":
    main()