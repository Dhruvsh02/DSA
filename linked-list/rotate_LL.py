# rotate a linked list 
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def rotate_linked_list(head,k):
    if head is None or k == 0:
        return head 
    length = 1
    tail = head 
    while tail.next:
        tail = tail.next
        length += 1
    if k % length == 0:
        return head 
    k = k % length
    tail.next = head
    new_tail = nth_node(head,length - k)
    head = new_tail.next 

    new_tail.next = None
    return head
def nth_node(head,n):
    temp = head 
    count = 1 
    while temp and count < n:
        temp = temp.next 
        count += 1
    return temp

def main():
    arr = [1,2,3,4,5,6,7,8,9]
    k = 3
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node

    head = rotate_linked_list(head,k)
    print(f"Linked list after rotating by {k} positions:")
    temp = head
    while temp:
        print(temp.data, end="->" if temp.next else "\n")
        temp = temp.next    
if __name__ == "__main__":
    main()

    
