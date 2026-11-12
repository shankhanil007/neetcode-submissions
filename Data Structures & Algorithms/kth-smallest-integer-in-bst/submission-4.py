# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.counter = k

        def helper(curr):
            if not curr:
                return 
            
            helper(curr.left)
            
            self.counter -= 1
            if self.counter == 0:
                self.ans = curr.val
                return
                
            helper(curr.right)
        
        helper(root)
        return self.ans
            