class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(len(arr)):
            if i==0 and arr[i]!=1:
                arr[i]=1
            elif 1<=i<len(arr):
                if abs(arr[i]-arr[i-1])<=1:
                    continue
                else:
                    arr[i]=arr[i-1]+1
        return arr[-1]








        




        