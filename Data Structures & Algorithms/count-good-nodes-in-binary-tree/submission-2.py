# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.ans = 1

        def helper(curr, cmax):

            if not curr:
                return

            if curr.val >= cmax:
                self.ans += 1

            cmax = max(curr.val, cmax)

            helper(curr.left, cmax)
            helper(curr.right, cmax)
        
        helper(root.left, root.val)
        helper(root.right, root.val)

        return self.ans