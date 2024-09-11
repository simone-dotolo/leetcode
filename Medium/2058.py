# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        def is_critical(previous_val, next_val, current_val):
            return (current_val > next_val and current_val > previous_val) or (current_val < next_val and current_val < previous_val) 

        critical_list = []

        prev_val = head.val
        node = head.next
        count = 2

        while node:
            if node.next and is_critical(prev_val, node.next.val, node.val):
                critical_list.append(count)
            prev_val = node.val
            node = node.next

            count += 1
        
        if len(critical_list) < 2:
            return [-1, -1]
        
        ans = [0, 0]

        ans[1] = critical_list[-1] - critical_list[0]

        min_diff = ans[1]

        for i in range(len(critical_list)-1):
            if (critical_list[i+1] - critical_list[i]) < min_diff:
                min_diff = (critical_list[i+1] - critical_list[i])
        
        ans[0] = min_diff

        return ans