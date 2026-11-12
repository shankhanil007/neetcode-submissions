# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0

        def helper(node, maxi):
            if not node:
                return 
            
            if node.val >= maxi:
                self.count += 1
            
            maxi = max(maxi, node.val)

            helper(node.left, maxi)
            helper(node.right, maxi)
        
        helper(root, -float('inf'))

        return self.count

