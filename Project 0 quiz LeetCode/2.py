# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode() 
    current = dummy_head
    carry = 0  

    while l1 or l2 or carry:
        value1 = l1.value if l1 else 0
        value2 = l2.value if l2 else 0

        total_sum = value1 + value2 + carry
        carry, remainder = divmod(total_sum, 10)

        current.next = ListNode(remainder)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next  

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

# Case 1
l1 = list_to_linked_list([2, 4, 3])
l2 = list_to_linked_list([5, 6, 4])
result = add_two_numbers(l1, l2)
print(linked_list_to_list(result))

# Case 2
l1 = list_to_linked_list([0])
l2 = list_to_linked_list([0])
result = add_two_numbers(l1, l2)
print(linked_list_to_list(result))

# Case 3
l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linked_list([9, 9, 9, 9])
result = add_two_numbers(l1, l2)
print(linked_list_to_list(result))


