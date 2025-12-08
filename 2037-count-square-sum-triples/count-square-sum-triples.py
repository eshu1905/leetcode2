class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        arr=[]
        for i in range(1,n+1):
            arr.append(i*i)
        for i in range(1,n+1):
            for j in range(1,n+1):
                req=(i*i)+(j*j)
                if req in arr:
                    count+=1
        return count            



        