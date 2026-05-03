# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        inorder=[]
        def helper(root):
            if not root:
                return None
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
        helper(root)
        return inorder[k-1]
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        