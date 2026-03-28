# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
    
        q = deque([(root, 0)])
        max_width = 0
        
        while q:
            size = len(q)
            _, first = q[0]
            
            for _ in range(size):
                node, idx = q.popleft()
                
                if node.left:
                    q.append((node.left, 2*idx))
                if node.right:
                    q.append((node.right, 2*idx + 1))
            
            _, last = (node, idx)
            max_width = max(max_width, last - first + 1)
        
        return max_width
            