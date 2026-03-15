# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        result=[]
        while queue:
            size=len(queue)
            level=[]
            for _ in range(size):
                ele=queue.popleft()
                level.append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            result.append(level)
        return result

        
        
        