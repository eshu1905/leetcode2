class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n=len(costs)
        buys=0
        for i in range(n):
            if i==0 and costs[i]>coins:
                return 0
            if coins-costs[i]>=0:
                coins-=costs[i]
                buys+=1
        return buys


           

        