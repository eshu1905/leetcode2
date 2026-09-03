class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        x=min(nums1)
        if x&1:
            return True
        for i in nums1:
            if i&1:
                return False
        return True

        