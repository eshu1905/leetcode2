# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def length(root):
            if not root:
                return 0
            return 1+max(length(root.left),length(root.right))
        left=length(root.left)
        right=length(root.right)
        if abs(left-right)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        

        
        
                



        
        