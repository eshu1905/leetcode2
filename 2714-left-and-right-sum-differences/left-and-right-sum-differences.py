class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum=[]
        right_sum=[]
        n=len(nums)
        for i in range(n):
            if i==0:
                left_sum.append(0)
                right_sum.append(sum(nums[i+1:]))
            elif i==n-1:
                left_sum.append(sum(nums[:n-1]))
                right_sum.append(0)
            else:
                left_sum.append(sum(nums[:i]))
                right_sum.append(sum(nums[i+1:]))
        for i in range(n):
            nums[i]=abs(left_sum[i]-right_sum[i])
        return nums