class Solution(object):
    def maximumTripletValue(self, nums):
        maxi=float("-inf")
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    ans=(nums[i]-nums[j])*nums[k]
                    if ans>maxi:
                        maxi=ans
        return maxi if maxi>0 else 0                

        """
        :type nums: List[int]
        :rtype: int
        """
        