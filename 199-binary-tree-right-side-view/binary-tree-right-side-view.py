# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([(root,0)])
        side_view={}
        while q:
            node,hd=q.popleft()
            if hd not in side_view:
                side_view[hd]=node.val
            if node.right:
                q.append((node.right,hd+1))
            if node.left:
                q.append((node.left,hd+1))
        return [side_view[key] for key in sorted(side_view)]
        
        
        