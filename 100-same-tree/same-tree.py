# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        queue = deque([(p, q)])
    
        while queue:
            n1, n2 = queue.popleft()
        
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
        
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
    
        return True
    
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        