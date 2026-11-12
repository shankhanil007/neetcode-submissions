# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        ans = []

        def helper(node):
            if not node:
                ans.append('N')
                return
            
            ans.append(str(node.val))
            helper(node.left)
            helper(node.right)

        helper(root)
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        arr = data.split(",")
        idx = 0

        def helper():
            nonlocal idx

            if arr[idx] == 'N':
                idx += 1
                return None

            node = TreeNode(arr[idx])
            idx += 1
            node.left = helper()
            node.right = helper()

            return node
        return helper()
