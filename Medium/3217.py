# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        while curr:
            if curr.next and curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next

        if head.val in nums:
            return head.next
        else:
            return head