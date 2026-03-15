# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        postorder = []
        curr = root
        last_visited = None

        while curr or stack:
        
        # go left
            while curr:
                stack.append(curr)
                curr = curr.left
        
            node = stack[-1]

        # if right exists and not processed
            if node.right and last_visited != node.right:
                curr = node.right
            else:
                postorder.append(node.val)
                last_visited = stack.pop()

        return postorder