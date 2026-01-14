class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        seen={}
        for i in nums2:
            while stack and i>stack[-1]:
                prev=stack.pop()
                seen[prev]=i
            stack.append(i)
        while stack:
            seen[stack.pop()]=-1
        res=[]
        for  i in nums1:
            res.append(seen[i])
        return res        

             