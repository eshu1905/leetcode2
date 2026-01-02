from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        length=len(nums)
        n=length//2
        dictit=Counter(nums)
        for i,j in dictit.items():
            if j==n:
                return i


        