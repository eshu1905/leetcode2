class Solution:
    from collections import Counter
    def maxNumberOfBalloons(self, text: str) -> int:
        n=len(text)
        b="balloon"
        for i in b:
            if i not in text:
                return 0
        d=Counter(text)
        instance=0
        for i in range(n):
            count=0
            for i in b:
                if d[i]>0:
                    d[i]-=1
                else:
                    return instance
            instance+=1







        

        