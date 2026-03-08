class Solution(object):
    def findDifferentBinaryString(self, nums):
        n=len(nums[0])
        result=[]

        def backtrack(path):
            if len(path) == n:
                result.append(path)
                return

            backtrack(path + "0")
            backtrack(path + "1")

        backtrack("")
        for i in result:
            if i not in nums:
                return i
        return ""
        

        """
        :type nums: List[str]
        :rtype: str
        """
        