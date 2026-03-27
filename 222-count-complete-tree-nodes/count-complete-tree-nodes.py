# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        def dfs(root):
            if not root:
                return 
            return 1+max(0,dfs(root.left))+max(0,dfs(root.right))
        return dfs(root)
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        