# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(curr):

            if not curr:
                return []
            left = helper(curr.left)
            right = helper(curr.right)
            arr = [curr.val]
            for elem in left:
                if elem >= curr.val:
                    arr.append(elem)
            for elem in right:
                if elem >= curr.val:
                    arr.append(elem)
            
            return arr
        
        ans = helper(root)

        return len(ans)
