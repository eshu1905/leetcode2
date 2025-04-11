class Solution(object):
    def countSymmetricIntegers(self, low, high):
        result = 0
        for i in range(low, high+1):
            if i > 10 and i < 100:
                if i % 11 == 0:
                    result += 1
            elif i > 1000 and i < 10000:
                first = i // 1000 + i // 100 % 10
                last = i // 10 % 10 + i % 10
                if first == last:
                    result +=1
        return result                       
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        