# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node, i, max_h):
            if node is None:
                return i
            else:
                i += 1
                max_h = max(max_h, height(node.right, i, max_h), height(node.left, i, max_h))
                return max_h

        def is_balanced(node):
            if node is None:
                return True
            else:
                hl = height(node.left, 0, 0)
                hr = height(node.right, 0, 0)
                if abs(hl - hr) > 1:
                    return False
                return is_balanced(node.right) and is_balanced(node.left)
        
        return is_balanced(root)
