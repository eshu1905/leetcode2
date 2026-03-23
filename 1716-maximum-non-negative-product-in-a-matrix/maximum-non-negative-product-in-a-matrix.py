class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        
        matrix_negative = [[grid[0][0] for _ in range (n)] for _ in range(m)]
        matrix_positive = [[grid[0][0] for _ in range (n)] for _ in range(m)]

        for j in range(1, n):
            matrix_negative[0][j] =  (grid[0][j] * matrix_negative[0][j - 1])
            matrix_positive[0][j] =  (grid[0][j] * matrix_positive[0][j - 1])
        
        for i in range(1, m):
            matrix_negative[i][0] = (grid[i][0] * matrix_negative[i - 1][0])
            matrix_positive[i][0] = (grid[i][0] * matrix_positive[i - 1][0])

        for i in range(1, m):
            for j in range(1, n):
                matrix_positive[i][j] = max(
                    matrix_positive[i - 1][j] * grid[i][j],
                    matrix_positive[i][j - 1] * grid[i][j],
                    matrix_negative[i - 1][j] * grid[i][j],
                    matrix_negative[i][j - 1] * grid[i][j]
                    )

                matrix_negative[i][j] = min(
                    matrix_negative[i - 1][j] * grid[i][j],
                    matrix_negative[i][j - 1] * grid[i][j],
                    matrix_positive[i - 1][j] * grid[i][j],
                    matrix_positive[i][j - 1] * grid[i][j]
                ) 
        
        res = matrix_positive[m - 1][n - 1]

        return res % MOD if res >= 0 else -1
        