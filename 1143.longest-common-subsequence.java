/*
 * @lc app=leetcode id=1143 lang=java
 *
 * [1143] Longest Common Subsequence
 */

// @lc code=start
class Solution {
    public int solution(int r, int c, int row, int col, String text1, String text2, int [][] dp) {
        if ((r == row) || (c == col)) {
            return 0;
        }
        if (dp[r][c] != -1) {
            return dp[r][c];
        }

        if (text1.charAt(r) == text2.charAt(c)) {
            dp[r][c] = 1 + solution(r + 1, c + 1, row, col, text1, text2, dp);
        } else {
            dp[r][c] = Math.max(solution(r, c + 1, row, col, text1, text2, dp), solution(r + 1, c, row, col, text1, text2, dp));
        }
        return dp[r][c];
    }

    public int longestCommonSubsequence(String text1, String text2) {
        int row = text1.length(), col = text2.length();
        int dp[][] = new int[row][col];
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j ++) {
                dp[i][j] = -1;
            }
        } 
        return solution(0, 0, row, col, text1, text2, dp);
    }
}
// @lc code=end

