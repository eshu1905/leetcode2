class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        total=0
        minimum=min(nums)
        maximum=max(nums)
        val=maximum-minimum
        return val*k

        