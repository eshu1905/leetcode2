class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxi=0
        ares=""
        for i in range(len(s)):
            count=0
            res=""
            for j in range(i,len(s)):
                if s[j] not in res:
                    res+=s[j]
                    count+=1
                else:
                    break
            if count>maxi:
                maxi=count
                ares=res
        return len(ares)                   



        """
        :type s: str
        :rtype: int
        """
        