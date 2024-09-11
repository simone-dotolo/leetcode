# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        node = l1
        while node.next != None:
            n1 += str(node.val) 
            node = node.next
        n1 += str(node.val)

        n2 = ''
        node = l2
        while node.next != None:
            n2 += str(node.val)
            node = node.next
        n2 += str(node.val)

        n1 = int(n1[::-1])
        n2 = int(n2[::-1])

        n_res = str(n1 + n2)[::-1]

        node_list = [ListNode(i) for i in n_res]

        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]

        return node_list[0]