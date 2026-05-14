# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        inorder=sorted(preorder)
        def helper(preorder,inorder):
            if inorder:
                ind=inorder.index(preorder.pop(0))
                root=TreeNode(inorder[ind])
                root.left=helper(preorder,inorder[0:ind])
                root.right=helper(preorder,inorder[ind+1:])
                return root
        h=helper(preorder,inorder)
        return h
        #return root

        





        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        