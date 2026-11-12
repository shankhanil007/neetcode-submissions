# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = -float('inf')

        def helper(node):
            nonlocal ans

            if not node:
                return 0

            left_sum = helper(node.left)
            right_sum = helper(node.right)

            temp = max(left_sum, 0) + max(right_sum, 0) + node.val  ### IIMMPP
            ans = max(ans, temp)

            return max(left_sum, right_sum, 0) + node.val

        helper(root)

        return ans
        