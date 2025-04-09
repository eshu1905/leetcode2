class Solution(object):
    def minOperations(self, nums, k):
        seen=set(nums)
        h=min(nums)
        if h<k:
            return -1
        elif h>k:
            return len(seen)
        else:
            return len(seen)-1        
        
        