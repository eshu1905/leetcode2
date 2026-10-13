# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result=[]
        def dfs(node,re,path):
            if node is None:
                return 
            path.append(node.val)
            re-=node.val
            if node.left is None and node.right is None:
                if re==0:
                    result.append(path[:])
            else:
                dfs(node.left,re,path)
                dfs(node.right,re,path)
            path.pop()
        dfs(root,targetSum,[])
        return result
        