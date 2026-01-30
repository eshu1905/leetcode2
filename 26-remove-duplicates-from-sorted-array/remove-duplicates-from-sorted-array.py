class Solution(object):
    def removeDuplicates(self, nums):
        arr=[]
        for i in nums:
            if i not in arr:
                arr.append(i)
        for i in range(len(arr)):
            nums[i]=arr[i]
        return len(arr)
       

        """
        :type nums: List[int]
        :rtype: int
        """
        