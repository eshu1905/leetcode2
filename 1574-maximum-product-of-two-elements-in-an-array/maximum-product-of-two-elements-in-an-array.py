class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        maxi=nums[-1]
        second_maxi=nums[-2]
   
        return (second_maxi-1)*(maxi-1)

        