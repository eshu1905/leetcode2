class Solution(object):
    def minOperations(self, s):
        diff1 = 0  # pattern starting with '0'
        diff2 = 0  # pattern starting with '1'
    
        for i in range(len(s)):
            if i%2 == 0:
                if s[i] == "0":
                    diff2+=1
                else:
                    diff1+=1
            else:
                if s[i] == "0":
                    diff1+=1
                else:
                    diff2+=1
    
        return min(diff1, diff2)
        """
        :type s: str
        :rtype: int
        """
        