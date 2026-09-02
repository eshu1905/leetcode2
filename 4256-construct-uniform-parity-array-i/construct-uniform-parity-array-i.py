class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n=len(nums1)
        even_n=[]
        odd_n=[]
        j=0
        for i in range(n):
            if j<n and i<j:
                j+=1
            x=nums1[i]
            if x%2==0:
                even_n.append(x)
                odd_n.append(x-nums1[j])
            else:
                odd_n.append(x)
                even_n.append(x-nums1[j])
        return len(even_n)==n or len(odd_n)==n

        