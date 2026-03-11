class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        res=[]
        integer=n
        while integer!=0:
            res.append(integer%2)
            integer//=2
        
        ans=[]
        for i in res:
            if i==0:
                ans.append(1)
            else:
                ans.append(0)
        a_ans=0
        for i in range(len(ans)):
            a_ans+=(2**i)*ans[i]
        return a_ans




        