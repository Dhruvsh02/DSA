# flattening a linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

# brute force approach
def flatten_linked_list(head):
    if head is None:
        return None 
    arr = []
    temp = head 
    while temp:
        t2 = temp 
        while t2:
            arr.append(t2.data)
            t2= t2.child 
        temp = temp.next
    arr.sort()
    new_head = Node(arr[0])
    current = new_head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node 
    return new_head

# optimized approach using two pointers in vertical manner
def merge_two_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    dummy = Node(-1)
    res = dummy 
    while list1 and list2:
        if list1.data < list2.data:
            res.child = list1
            res = list1
            list1 = list1.next
        else:
            res.child = list2
            res = list2
            list2 = list2.next
        res.next = None
    if list1:
        res.child = list1
    if list2:
        res.child = list2
    return dummy.child

def flatten_linked_list_optimized(head):
    if head is None or head.next is None:
        return head 
    head.next = flatten_linked_list_optimized(head.next)
    head = merge_two_lists(head, head.next)
    return head


def main():
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(19)
    head.next.next.next = Node(28)

    head.child = Node(7)
    head.child.child = Node(8)
    head.child.child.child = Node(30)

    head.next.child = Node(20)

    head.next.next.child = Node(22)
    head.next.next.child.child = Node(50)

    head.next.next.next.child = Node(35)
    head.next.next.next.child.child = Node(40)
    head.next.next.next.child.child.child = Node(45)

    head = flatten_linked_list_optimized(head)
    print("Flattened linked list:")
    temp = head
    while temp:
        print(temp.data, end="->" if temp.next else "\n")
        temp = temp.next
if __name__ == "__main__":
    main()