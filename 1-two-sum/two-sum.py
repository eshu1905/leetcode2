class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        n=len(nums)
        for i in range(n):
            more=target-nums[i]
            if more in map:
                return [i,map[more]]
            map[nums[i]]=i




        





        