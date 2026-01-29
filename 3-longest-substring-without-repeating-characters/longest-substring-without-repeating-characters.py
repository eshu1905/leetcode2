class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxi = 0
        seen = {}

        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right
            maxi = max(maxi, right - left + 1)
            right += 1

        return maxi
              
               


        


        
        