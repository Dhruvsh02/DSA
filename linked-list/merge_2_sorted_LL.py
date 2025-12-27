# merge two sorted linked lists 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    

# brute force approach
def merge_sorted_linked_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    temp1 = head1
    temp2 = head2
    arr = []
    while temp1:
        arr.append(temp1.data)
        temp1 = temp1.next
    while temp2:
        arr.append(temp2.data)
        temp2 = temp2.next
    arr.sort()
    new_head = Node(arr[0])
    current = new_head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    return new_head

# optimized approach using two pointers
def merge_sorted_linked_lists_optimized(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    t1 = head1
    t2 = head2
    dummy = Node(-1)
    temp = dummy
    while t1 and t2:
        if t1.data < t2.data:
            temp.next = t1
            t1 = t1.next
        else:
            temp.next = t2
            t2 = t2.next
        temp = temp.next 
    if t1:
        temp.next = t1
    if t2:
        temp.next = t2
    new_head = dummy.next
    return new_head

def main():
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    head1 = Node(arr1[0])
    current = head1
    for val in arr1[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node

    head2 = Node(arr2[0])
    current = head2
    for val in arr2[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node

    merged_head = merge_sorted_linked_lists_optimized(head1, head2)
    print("Merged linked list:")
    temp = merged_head
    while temp:
        print(temp.data, end="->" if temp.next else "\n")
        temp = temp.next
if __name__ == "__main__":
    main()