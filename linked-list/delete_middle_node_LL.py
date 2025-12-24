# delete the middle node of a linked list
# brute force approach : calculate length first then delete middle node

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def delete_middle_node_ll(head):
    if head is None or head.next is None:
        return None 
    length = 0 
    temp = head 
    while temp:
        length += 1
        temp = temp.next 
    mid_index = length // 2
    temp = head 
    while mid_index - 1 > 0:
        temp = temp.next
        mid_index -= 1
    temp.next = temp.next.next
    return head

# optimal approach : slow and fast pointer
def delete_middle_node_ll_optimal(head):
    if head is None or head.next is None:
        return None
    slow = head 
    fast = head
    fast = fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head


def main():
    arr = [1,2,3,4,5]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    print("Original Linked List:")
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
    
    head = delete_middle_node_ll_optimal(head)
    
    print("Linked List after deleting middle node:")
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
if __name__ == "__main__":
    main()