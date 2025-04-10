class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        def baho(num):
            count = 0
            strNum=str(num)

            for i in range(len(strNum)-len(s)):
                count += min(limit + 1, int(strNum[i])) * (limit + 1) ** (len(strNum) - len(s) - i - 1)
                if int(strNum[i]) > limit:
                    break
            else:
                count += (int(strNum[-len(s):]) >= int(s))
            return count

        return baho(finish) - baho(start-1)
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        