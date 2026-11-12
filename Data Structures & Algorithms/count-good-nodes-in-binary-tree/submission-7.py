# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0

        def helper(node, cmax):
            if not node:
                return

            if node.val >= cmax:
                cmax = node.val
                self.count += 1

            helper(node.left, cmax)
            helper(node.right, cmax)
        
        helper(root, -float('inf'))

        return self.count