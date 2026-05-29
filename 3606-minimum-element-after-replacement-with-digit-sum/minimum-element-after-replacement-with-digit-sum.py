class Solution:
    def minElement(self, nums: List[int]) -> int:
        def add(n):
            digit=0
            while n!=0:
                last=n%10
                digit+=last
                n=n//10
            return digit
        arr=[]
        n=len(nums)
        for i in range(n):
            arr.append(add(nums[i]))
        return min(arr)

        