# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if inorder:
            index=inorder.index(postorder.pop(-1))
            root=TreeNode(inorder[index])
            root.right=self.buildTree(inorder[index+1:],postorder)
            root.left=self.buildTree(inorder[0:index],postorder)
           
            return root
       



        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        