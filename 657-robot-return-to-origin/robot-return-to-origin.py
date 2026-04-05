class Solution(object):
    def judgeCircle(self, moves):
        up,down,left,right=0,0,0,0
        n=len(moves)
        for i in range(n):
            if moves[i]=="U":
                up+=1
            elif moves[i]=="D":
                down+=1
            elif moves[i]=="L":
                left+=1
            else:
                right+=1
        if up ==down and left==right:
            return True
        else:
            return False
        """
        :type moves: str
        :rtype: bool
        """
        