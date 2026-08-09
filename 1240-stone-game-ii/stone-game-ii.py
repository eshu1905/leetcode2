class Solution:
    def __init__(self):
        self.t = dict()

    def solveForAlice(self, piles: List[int], person: int, i: int, M: int):
        size = len(piles)
        if i >= size:
            return 0
        key = str(person) + '-' + str(i) + '-' + str(M)
        checkVal = self.t.get(key)
        if checkVal is not None:
            return checkVal

        result = -1 if person == 1 else float("inf")
        stones = 0

        for x in range(1, min(2*M, size - i) + 1):
            stones += piles[i + x - 1]
            if person == 1:
                result = max(result, stones + self.solveForAlice(piles, 0, i+x, max(M, x)))
            else:
                result = min(result, self.solveForAlice(piles, 1, i+x, max(M, x)))
        self.t[key] = result
        return result

    def stoneGameII(self, piles: List[int]) -> int:
        dic = dict()
        return self.solveForAlice(piles, 1, 0, 1)

        