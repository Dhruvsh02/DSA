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


# optimal appraoch 

def reverse_ll_optimal(head):
    prev = None
    temp = head 
    front = None
    while temp:
        front = temp.next
        temp.next = prev 
        prev = temp
        temp = front
    return prev

def is_palindrome_ll_optimal(head):
    if head == None or head.next == None:
        return True
    slow, fast = head, head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    new_head = reverse_ll_optimal(slow.next)
    first = head
    second = new_head
    while second != None:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
    slow.next = reverse_ll_optimal(new_head)
    return True

def main():
    arr = [1,2,3,2]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = current.next
    if is_palindrome_ll_optimal(head):
        print("Palindrome")
    else:
        print("Not a Palindrome")
if __name__ == "__main__":
    main()