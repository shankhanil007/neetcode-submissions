# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(curr, cmin, cmax):
            if not curr:
                return True

            if curr.val <= cmin or curr.val >= cmax:
                return False

            left = helper(curr.left, cmin, curr.val)
            right = helper(curr.right, curr.val, cmax)

            return left and right

        return helper(root, -float("inf"), float("inf"))