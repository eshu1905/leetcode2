class Solution(object):
    def countGoodNumbers(self, n):
        mod = 10**9 + 7

        # use fast exponentiation to calculate x^y % mod
        def quickmul(x,y):
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //= 2
            return ret

        return quickmul(5, (n + 1) // 2) * quickmul(4, n // 2) % mod
        

        """
        :type n: int
        :rtype: int
        """
        