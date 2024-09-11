# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]

        i = 0
        j = 0
        delta_i = 0
        delta_j = 1
        curr = head
        upper_lim = 0
        lower_lim = m - 1
        sx_lim = 0
        dx_lim = n - 1
        while curr:
            res[i][j] = curr.val
            curr = curr.next
            if j == dx_lim and delta_j == 1:
                delta_i = 1
                delta_j = 0
                upper_lim += 1
            elif j == sx_lim and delta_j == -1:
                delta_i = -1
                delta_j = 0
                lower_lim -= 1
            elif i == lower_lim and delta_i == 1:
                delta_i = 0
                delta_j -= 1
                dx_lim -= 1
            elif i == upper_lim and delta_i == -1:
                delta_i = 0
                delta_j = 1
                sx_lim += 1
            i += delta_i
            j += delta_j
        
        return res
        