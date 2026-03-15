# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        curr=root
        stack=[]
        inorder=[]
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            node=stack.pop()
            inorder.append(node.val)
            curr=node.right
        return inorder

            
        
           


        