# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []

        queue = deque([root])

        while queue:
            # code logic for problem
            level = []
            levelSize = len(queue)

            # bfs logic
            for i in range(len(queue)):
                n = queue.popleft()
                level.append(n.val)

                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
            
            res.append(level)
            
        return res
