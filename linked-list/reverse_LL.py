# reverse a linked list 
# brute force apporach using stack data structure

class Node: 
    def __init__(self,data):
        self.data = data 
        self.next = None

def reverse_ll(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head 
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head

# optimal approach : one traversal

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

# recursive approach

def reverse_ll_recursive(head):
    if head == None or head.next == None:
        return head 
    new_head = reverse_ll_recursive(head.next)
    front = head.next
    front.next = head
    head.next = None 
    return new_head


def main():
    arr = [1,2,3,4,5]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = current.next
    head = reverse_ll_recursive(head)
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()