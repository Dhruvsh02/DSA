# detect a loop or cycle in a linked list

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# brute force approach : using hash set
def detect_loop_ll(head):
    nodes_set = set()
    temp = head 
    while temp:
        if temp in nodes_set:
            return True 
        nodes_set.add(temp)
        temp = temp.next 
    return False

# optimal approach : tortoise and hare algorithm - slow and fast pointer
def detect_loop_ll_optimal(head):
    if head is None :
        return None 
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def main():
    arr = [1,2,3,4,5,6,3]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    current.next = head.next.next
    if detect_loop_ll(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

if __name__ == "__main__":
    main()