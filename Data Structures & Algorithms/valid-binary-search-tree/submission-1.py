# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(curr, low, high):
            if not curr:
                return True
            
            if curr.val <= low or curr.val >= high:
                return False
            
            left = helper(curr.left, low, curr.val)
            right = helper(curr.right, curr.val, high)

            if left and right:
                return True

            return False

        return helper(root, float("-inf"), float("inf"))