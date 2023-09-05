def uniquePathsWithObstacles(obstacleGrid):
    if (len(obstacleGrid) == 0 or obstacleGrid[0][0] == 1):
        return 0

    rows, cols = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * cols
    dp[0] = 1

    for r in range(rows):
        for c in range(cols):
            if obstacleGrid[r][c] == 1:
                dp[c] = 0
            else:
                if c > 0:
                    dp[c] += dp[c - 1]
    return dp[cols - 1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(obstacleGrid))
