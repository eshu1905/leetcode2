class Solution:
    def rob(self, nums: List[int]) -> int:
        x,y=0,0
        for i in nums:
            y,x=x,max(x,y+i)
        return x
        