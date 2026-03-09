class Solution(object):
    def lemonadeChange(self, bills):
        five=0
        ten=0
        twenty=0
        n=len(bills)
        for i  in range(n):
            if i==0 and (bills[i]==10 or bills[i]==20):
                return False
            elif bills[i]==5:
                five+=1
            elif bills[i]==10:
                ten+=1
                if five:
                    five-=1
                else:
                    return False
            else:
                twenty+=1
                if ten and five:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                elif ten and five>1:
                    five-=1
                    ten-=1
                else:
                    return False
        return True

                    
        """
        :type bills: List[int]
        :rtype: bool
        """
        