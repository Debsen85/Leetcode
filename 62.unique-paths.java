/*
 * @lc app=leetcode id=62 lang=java
 *
 * [62] Unique Paths
 */

// @lc code=start

class Solution {

    public int uniquePath(int i, int j, int m, int n, int [][] dp) {
        if ((i == m) || (j == n)) {
            return 0;
        }
        if ((i == m - 1) && (j == n - 1)) {
            return 1;
        }
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        
        dp[i][j] = uniquePath(i + 1, j, m, n, dp) + uniquePath(i, j + 1, m, n, dp);

        return dp[i][j];
    }

    public int uniquePaths(int m, int n) {
        int dp[][] = new int[m][n];
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                dp[i][j] = -1;
            }
        }
        return uniquePath(0, 0, m, n, dp);
    }
}
// @lc code=end

