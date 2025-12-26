# find pairs in sorted doubly linked list whose sum is equal to given value

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
# brute force approach : two nested loops
def pair_sum_sorted_dll(head, target_sum):
    temp1 = head 
    list = []
    while temp1:
        temp2 = temp1.next 
        while temp2 and temp1.data + temp2.data <= target_sum:
            if temp1.data + temp2.data == target_sum:
                list.append((temp1.data, temp2.data))
            temp2 = temp2.next 
        temp1 = temp1.next
    return list
# optimal approach : two pointer technique
def tail(head):
    temp = head 
    while temp.next:
        temp = temp.next
    return temp 
def pair_sum_sorted_dll_optimal(head, target_sum):
    if head is None:
        return None 
    left = head 
    right = tail(head)
    pairs = []
    while left.prev !=  right and left != right:
        current_sum = left.data + right.data
        if current_sum == target_sum:
            pairs.append((left.data,right.data))
            left = left.next
            right = right.prev
        elif current_sum > target_sum:
            right = right.prev 
        else:
            left = left.next
    return pairs
        
def main():
    arr = [1,2,3,4,5,6,7,8,9]
    target_sum = 10
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node

    pairs = pair_sum_sorted_dll_optimal(head, target_sum)
    if pairs:
        print(f"Pairs in the sorted doubly linked list with sum {target_sum}:")
        for pair in pairs:
            print(pair)
    else:
        print(f"No pairs found in the sorted doubly linked list with sum {target_sum}.")

if __name__ == "__main__":
    main()