class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        res=[]
        for i in range(n):
            if i+k<=n:
                res.append(nums[i:i+k])
        s=list(set(nums))
        counts={}
        for i in s:
            count=0
            for j in res:
                if i in j:
                    count+=1
            counts[i]=count
        mini=[]
        for i ,j in counts.items():
            if j==1:
                mini.append(i)
        if len(mini)==0:
            return -1
        return max(mini)
        

        
        