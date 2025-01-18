/*
 * @lc app=leetcode id=62 lang=java
 *
 * [62] Unique Paths
 */

// @lc code=start

class Solution {

    static int[][] cache;

    public static int help(int m, int n, int r, int c, int [][] cache) {
        if (r == m || c == n) {
            return 0;
        }
        if (r == m  - 1 && c == n - 1) {
            return 1;
        }
        if (cache[r][c] != 0) {
            return cache[r][c];
        }
        cache[r][c] = help(m, n, r + 1, c, cache) + help(m, n, r, c + 1, cache);
        return cache[r][c];
    }

    public int uniquePaths(int m, int n) {
        cache = new int[m][n];
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                cache[i][j] = 0;
            }
        }
        return help(m, n, 0, 0, cache);
    }
}
// @lc code=end

