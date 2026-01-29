class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        maxi=0
        
        for i in range(len(s)):
            sub_string=""
            for j in range(i,len(s)):
                if s[j] not in sub_string:
                    sub_string+=s[j]
                    if len(sub_string)>maxi:
                        maxi=len(sub_string)
                else:
                    break
        return maxi

               


        


        
        