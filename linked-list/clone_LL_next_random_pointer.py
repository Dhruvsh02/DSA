# clone a linked list wit next and random pointer / copy list with random pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None 
# brute force approach using hash map
def clone_linked_list(head):
    if head is None:
        return None
    temp = head 
    hash_map = {}
    while temp:
        new_node = Node(temp.data)
        hash_map[temp] = new_node
        temp = temp.next

    temp = head
    while temp:
        copy_node = hash_map[temp]
        copy_node.next = hash_map.get(temp.next)
        copy_node.random = hash_map.get(temp.random)
        temp = temp.next
    return hash_map[head]
    
# optimized approach without extra space
def clone_linked_list_optimized(head):
    if head is None:
        return None
    # step-1 insert copy nodes in between original nodes
    temp = head
    while temp:
        new_node = Node(temp.data)
        new_node.next = temp.next
        temp.next = new_node
        temp = new_node.next
    # step-2 connect random pointers
    temp = head
    while temp:
        new_node = temp.next
        new_node.random = temp.random.next if temp.random else None
        temp = temp.next.next
    # step-3 connect next pointers and separate lists
    temp = head
    dummy = Node(-1)
    res = dummy 
    while temp:
        res.next = temp.next
        temp.next = temp.next.next
        res = res.next
        temp = temp.next
    return dummy.next

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next

    cloned_head = clone_linked_list_optimized(head)
    temp = cloned_head
    while temp:
        random_data = temp.random.data if temp.random else None
        print(f'Node data: {temp.data}, Random points to: {random_data}')
        temp = temp.next

if __name__ == "__main__":
    main()