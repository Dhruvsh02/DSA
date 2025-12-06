# reverse a doubly linked list 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
# brute force approach : using stack 

def reverse_dll(head):
    temp = head  
    stack = []
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head

def main():
    arr = [10,20,30,40]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]: 
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next
    head = reverse_dll(head)
    temp = head 
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()


# optimal approach : one traversal 

def reverse_dll_swapping(head):
    if head == None and head.next == None:
        return head
    last = None
    current = head 
    while current:
        last = current.prev 
        current.prev = current.next
        current.next = last 
        current = current.prev 
    return last.prev 


def main():
    arr = [2,6,7,9]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next

    head = reverse_dll_swapping(head)
    temp = head 
    while temp:
        print(temp.data,end = "<->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()