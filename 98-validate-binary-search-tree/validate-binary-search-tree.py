# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        inorder=[]
        def helper(root):
            if not root:
                return None
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
        helper(root)
        for i in range(len(inorder)-1):
            if inorder[i]>=inorder[i+1]:
                return False
        return True

        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        