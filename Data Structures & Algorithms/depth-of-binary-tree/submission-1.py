# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.ans = -1

        def helper(curr, depth):

            if not curr:
                self.ans = max(depth, self.ans)
                return

            helper(curr.left, depth+1)
            helper(curr.right, depth+1)

        helper(root, 0)
        return self.ans