# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from math import log, ceil, inf
        
        def traverse(sums, node, level):
            if node is not None:
                if sums[level] == -inf:
                    sums[level] = node.val
                else:
                    sums[level] += node.val
                traverse(sums, node.left, level + 1)
                traverse(sums, node.right, level + 1)
                
        sums = [-inf for _ in range(int(1e4))]

        traverse(sums, root, 1)

        max_val = -inf
        max_index = -1
        for i in range(len(sums)):
            if sums[i] > max_val:
                max_val = sums[i]
                max_index = i
                
        return max_index
