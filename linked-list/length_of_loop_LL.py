# find the leght of the loop in liknked list 
# brute force approach using hashmap 
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def length_of_loop_ll(head):
    nodes_set = set()
    temp = head 
    timer = 1 
    while temp:
        if temp in nodes_set:
            value = temp.data
            return timer - value 
        nodes_set.add(temp)
        timer += 1
        temp = temp.next 
    return 0


# optimal approach : tortoise and hare algorithm - slow and fast pointer
def length_of_loop_ll_optimal(head):
    if head is None:
        return 0 
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 0
            while True:
                count += 1
                slow = slow.next
                if slow == fast:
                    break 
            return count
    return 0

def main():
    arr = [1,2,3,4,5,6,3]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    current.next = head.next.next
    loop_length = length_of_loop_ll_optimal(head)
    if loop_length:
        print(f"Length of loop detected in the linked list is: {loop_length}")
    else:
        print("No loop detected in the linked list.")

if __name__ == "__main__":
    main()
