# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []

        def helper(curr):
            if not curr:
                return 

            if not curr.left and not curr.right:
                self.arr.append(curr.val)
                return
            
            helper(curr.left)
            self.arr.append(curr.val)
            helper(curr.right)
        
        helper(root)

        return self.arr[k-1]
            