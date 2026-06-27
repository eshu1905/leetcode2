class Solution:
    from collections import Counter
    def maximumLength(self, nums: List[int]) -> int:
        n=len(nums)
        d=Counter(nums)
        mx_l=0

        if 1 in d.keys():
            if d[1]%2!=0:
                mx_l=max(mx_l,d[1])
            else:
                mx_l=max(mx_l,d[1]-1)
        for x in sorted(d.keys()):
            if x==1:
                continue
            curr=x
            curr_l=0
            while  curr in d and d[curr]>=2:
                curr_l+=2
                curr=curr**2
            if curr in d and d[curr]>=1:
                curr_l+=1
            else:
                curr_l-=1
            mx_l=max(mx_l,curr_l)
        return mx_l













                

        