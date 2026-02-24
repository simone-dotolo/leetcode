# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node):
            return node.left is None and node.right is None

        def explore(node, curr, res):
            if node:
                curr = curr * 2 + node.val
                if is_leaf(node):
                    res += curr
                else:
                    res = explore(node.left, curr, res)
                    res = explore(node.right, curr, res)
                return res
            else:
                return res
        
        return explore(root, 0, 0)
