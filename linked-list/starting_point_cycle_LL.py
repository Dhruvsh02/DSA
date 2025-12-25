# find the starting point of the loop.cycle in the linked list 
# brute force approach using hashmap
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def starting_point_cycle_ll(head):
    nodes_set = set()
    temp = head 
    while temp:
        if temp in nodes_set:
            return temp 
        nodes_set.add(temp)
        temp = temp.next
    return None 

# optimal approach : tortoise and hare algorithm - slow and fast pointer
def starting_point_cycle_ll_optimal(head):
    if head is None:
        return None 
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            slow = head 
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

def main():
    arr = [1,2,3,4,5,6,3]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    current.next = head.next.next
    start_node = starting_point_cycle_ll_optimal(head)
    if start_node:
        print(f"Starting point of cycle detected at node with value: {start_node.data}")
    else:
        print("No cycle detected in the linked list.")

if __name__ == "__main__":
    main()