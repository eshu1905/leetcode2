class Solution(object):
    def findRelativeRanks(self, score):
        x = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    
        seen = {}
        for i in range(len(score)):
            seen[score[i]] = i   # store score -> original index
    
        seen = sorted(seen.items(), reverse=True)
    
        answer = [0] * len(score)
    
        for z, (s, index) in enumerate(seen):
            if z < 3:
                answer[index] = x[z]
            else:
                answer[index] = str(z + 1)
    
        return answer
     




        
        