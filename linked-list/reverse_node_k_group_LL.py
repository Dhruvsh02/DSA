# reverse nodes in k group size of linked list 

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def reverse(head):
    prev = None 
    curr = None 
    temp = head 
    while temp:
        curr = temp.next
        temp.next = prev 
        prev = temp 
        temp = curr
    return prev

def kth_node(head,k):
    temp = head 
    count = 1
    while temp and count < k:
        temp = temp.next
        count += 1
    return temp

def reverse_k_group(head,k):
    prevnode = None
    temp = head 
    nextnode = None 
    while temp:
        kth = kth_node(temp,k)
        if not kth:
            if prevnode:
                prevnode.next = temp
            break
        nextnode = kth.next
        kth.next = None
        kth= reverse(temp)
        if temp == head:
            head = kth
        else:
            prevnode.next = kth
        
        prevnode = temp
        temp = nextnode

    return head

def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    k = 3
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node

    head = reverse_k_group(head,k)
    print(f"Linked list after reversing in groups of {k}:")
    temp = head
    while temp:
        print(temp.data, end="->" if temp.next else "\n")
        temp = temp.next
if __name__ == "__main__":
    main()