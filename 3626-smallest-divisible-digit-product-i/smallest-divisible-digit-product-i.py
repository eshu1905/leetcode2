class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def answer(n,t):
            ans=1
            for i in str(n):
                ans*=int(i)
            if ans%t==0:
                return True
        for i in range(n,100+1):
            if answer(i,t):
                return i

         
        
        



        