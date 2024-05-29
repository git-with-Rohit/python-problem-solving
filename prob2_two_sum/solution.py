class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        carry, out = divmod(val1 + val2 + carry, 10)
        
        current.next = ListNode(out)
        current = current.next
        
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
    
    return dummy.next

# Example usage:
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# result = add_two_numbers(l1, l2)
# while result:
#     print(result.val, end=" ")
#     result = result.next  # Output: 7 0 8
