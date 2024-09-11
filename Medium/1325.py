# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def is_leaf(node):
            return (node.left == None and node.right == None)
        
        def all_els_target(node):
            if node is None:
                return True
            if is_leaf(node):
                return node.val == target
            if node.val == target:
                return all_els_target(node.left) and all_els_target(node.right)
            else:
                return False

        def remove(node):
            if node is None:
                return
            if node.left is not None and node.left.val == target:
                # Delete left sub-tree if all elements are target
                if all_els_target(node.left):
                    node.left = None
                else:
                    remove(node.left)
            else:
                remove(node.left)
            if node.right is not None and node.right.val == target:
                # Delete left sub-tree if all elements are target
                if all_els_target(node.right):
                    node.right = None
                else:
                    remove(node.right)
            else:
                remove(node.right)
        
        remove(root)

        if is_leaf(root) and root.val == target:
            return None

        return root