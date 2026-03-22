# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#  
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        r = 1
    
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
    
        def level(root):
            if not root:
                return []
        
            queue = deque([(root, r)])
            result = []
        
            while queue:
                size = len(queue)
                ans = []

                for _ in range(size):
                    ele, pos = queue.popleft()
                    ans.append([ele.val, pos])   # store value, not node
                
                    if ele.left:
                        queue.append((ele.left, 2 * pos))
                    if ele.right:
                        queue.append((ele.right, 2 * pos + 1))
            
                result.append(ans)
        
            return result
    
        s1 = level(p)
        s2 = level(q)
    
        return s1 == s2
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        