# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            # base case
            if not node: return

            # swap children
            tmp = node.left
            node.left = node.right
            node.right = tmp

            # continue traversing the tree
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return root