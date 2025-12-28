# merge k sorted linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# brute force approach using array and sorting
def merge_lists(lists):
    if not lists:
        return None
    arr = []
    for head in lists:
        temp = head
        while temp:
            arr.append(temp.data)
            temp = temp.next
        arr.sort()
    new_head = Node(arr[0])
    current = new_head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    return new_head

# optimized approach using divide and conquer
def merge_two(l1, l2):
    dummy = Node(0)
    curr = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return dummy.next


def merge_lists_optimized(lists):
    if not lists:
        return None

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two(l1, l2))
        lists = merged

    return lists[0]

# optimal approach using min-heap
import heapq

def merge_lists_heap(lists):
    min_heap = []
    for head in lists:
        if head:
            heapq.heappush(min_heap, (head.data, head))
    dummy = Node(0)
    curr = dummy
    while min_heap:
        val, node = heapq.heappop(min_heap)
        curr.next = Node(val)
        curr = curr.next
        if node.next:
            heapq.heappush(min_heap, (node.next.data, node.next))
    return dummy.next

def main():
    arr1 = [1, 4, 7]
    arr2 = [2, 5, 8]
    arr3 = [3, 6, 9]
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
    head3 = Node(arr3[0])
    current = head3
    for val in arr3[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    lists = [head1, head2, head3]
    merged_head = merge_lists_optimized(lists)
    print("Merged k sorted linked lists:")
    temp = merged_head
    while temp:
        print(temp.data, end="->" if temp.next else "\n")
        temp = temp.next
if __name__ == "__main__":
    main()