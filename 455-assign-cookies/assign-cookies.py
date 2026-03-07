class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        left=0
        right=0
        while right<len(s) and left<len(g):
            if s[right]>=g[left]:
                left+=1
            right+=1
        return left
            


                

           







        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        