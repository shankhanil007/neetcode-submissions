# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #### Approach 1: each node sends back list of filtered goodNodes

        # def helper(curr):
        #     if not curr:
        #         return []
        #     left = helper(curr.left)
        #     right = helper(curr.right)
        #     arr = [curr.val]
        #     for elem in left:
        #         if elem >= curr.val:
        #             arr.append(elem)
        #     for elem in right:
        #         if elem >= curr.val:
        #             arr.append(elem)
            
        #     return arr
        
        # ans = helper(root)
        # return len(ans)


        #### Approach 2 Preorder traversal + maxVal seen so far + sum of good nodes on left and right

        def helper(curr, maxi):

            if not curr:
                return 0

            if curr.val >= maxi:
                res = 1
            else:
                res = 0
            maxi = max(curr.val, maxi)
            res += helper(curr.left, maxi)
            res += helper(curr.right, maxi)

            return res
        
        return helper(root, root.val)
