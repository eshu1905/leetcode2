class Solution:
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_beauty = 0
        n = len(s)
        
        for i in range(n):
            # Frequency array for the substring s[i...j]
            freq = [0] * 26
            
            for j in range(i, n):
                # Update frequency for the new character
                freq[ord(s[j]) - ord('a')] += 1
                
                min_freq = float('inf')
                max_freq = float('-inf')
                
                # Find min and max in the current frequency array
                for k in range(26):
                    if freq[k] > 0: # Only consider present characters
                        min_freq = min(min_freq, freq[k])
                        max_freq = max(max_freq, freq[k])
                
                # Add the beauty of the current substring s[i...j]
                total_beauty += (max_freq - min_freq)
                
        return total_beauty
        """
        :type s: str
        :rtype: int
        """
        