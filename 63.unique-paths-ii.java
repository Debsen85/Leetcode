/*
 * @lc app=leetcode id=63 lang=java
 *
 * [63] Unique Paths II
 */

// @lc code=start
class Solution {
    static int[][] cache;

    public static int help(int [][] obstacleGrid, int m, int n, int r, int c, int [][] cache) {
        if (r == m || c == n || obstacleGrid[r][c] == 1) {
            return 0;
        }
        if (cache[r][c] > 0) {
            return cache[r][c];
        }
        if (r == m  - 1 && c == n - 1) {
            return 1;
        }
        cache[r][c] = help(obstacleGrid, m, n, r + 1, c, cache) + help(obstacleGrid, m, n, r, c + 1, cache);
        return cache[r][c];
    }

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        if (obstacleGrid[m - 1][n - 1] == 1) {
            return 0;
        }
        cache = new int[m][n];
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                cache[i][j] = 0;
            }
        }
        return help(obstacleGrid, m, n, 0, 0, cache);
    }
}
// @lc code=end

