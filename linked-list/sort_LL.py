# sort a linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# brute force approach using array and sorting
def sort_linked_list(head):
    if head is None:
        return None
    arr = []
    temp = head
    while temp:
        arr.append(temp.data)
        temp = temp.next
    arr.sort()
    new_head = Node(arr[0])
    curr = new_head
    for val in arr[1:]:
        new_node = Node(val)
        curr.next = new_node
        curr = new_node
    return new_head
# optimized approach using merge sort
def merge_sort(head):
    if head is None or head.next is None:
        return head
    mid = get_middle(head)
    next_to_mid = mid.next
    mid.next = None
    left = merge_sort(head)
    right = merge_sort(next_to_mid)
    sorted_list = sorted_merge(left, right)
    return sorted_list
def get_middle(head):
    if head is None:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
def sorted_merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    return result

def main():
    arr = [4, 2, 1, 3]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node

    head = merge_sort(head)
    print("Sorted linked list:")
    temp = head
    while temp:
        print(temp.data, end="->" if temp.next else "\n")
        temp = temp.next
if __name__ == "__main__":
    main()