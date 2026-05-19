class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        low1=0
        low2=0
        n1=len(nums1)
        n2=len(nums2)
        while low1<n1 and low2<n2:
            if nums1[low1]==nums2[low2]:
                return nums1[low1]
            elif nums1[low1]<nums2[low2]:
                low1+=1
            else:
                low2+=1
        return -1
        