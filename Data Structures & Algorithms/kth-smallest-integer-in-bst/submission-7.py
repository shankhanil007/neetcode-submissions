# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.counter = 0
        self.ans = -1

        def helper(root):
            if not root or self.ans != -1:
                return
            helper(root.left)
            self.counter += 1
            if self.counter == k:
                self.ans = root.val
            helper(root.right)
        
        helper(root)

        return self.ans