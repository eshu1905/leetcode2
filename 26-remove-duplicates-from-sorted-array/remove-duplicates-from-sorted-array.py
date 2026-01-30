class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        for i in range(len(nums)):
            if nums[k]!=nums[i]:
                k+=1
                nums[k],nums[i]=nums[i],nums[k]
        return k+1

        """
        :type nums: List[int]
        :rtype: int
        """
        