# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(a, b):
            if a == 0:
                return b
            return GCD(b % a, a)

        curr = head

        while curr and curr.next:
            next_node = curr.next
            gcd = GCD(curr.val, next_node.val)
            new_node = ListNode(val=gcd, next=next_node)
            curr.next = new_node
            curr = next_node
        
        return head