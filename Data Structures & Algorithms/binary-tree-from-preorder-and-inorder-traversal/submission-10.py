# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        index = {}
        for idx, node in enumerate(inorder):
            index[node] = idx
        
        self.pidx = 0

        def helper(left, right):

            if left > right:
                return None

            inidx = index[preorder[self.pidx]]
            val = preorder[self.pidx]
            self.pidx += 1
            node = TreeNode(val)
            node.left = helper(left, inidx - 1)
            node.right = helper(inidx+1, right)

            return node

        return helper(0, len(preorder)-1)