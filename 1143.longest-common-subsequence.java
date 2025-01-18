/*
 * @lc app=leetcode id=1143 lang=java
 *
 * [1143] Longest Common Subsequence
 */

// @lc code=start
class Solution {
    private static int[][] cache;
    private static int help(String text1, String text2, int i, int j) {
        if (i == text1.length() || j == text2.length()) {
            return 0;
        }
        if (cache[i][j] != -1) {
            return cache[i][j];
        }
        if (text1.charAt(i) == text2.charAt(j)) {
            cache[i][j] = 1 + help(text1, text2, i + 1, j + 1);
        } else {
            cache[i][j] = Math.max(help(text1, text2, i + 1, j), help(text1, text2, i, j + 1));
        }
        return cache[i][j];   
    }
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        cache = new int[m][n];
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                cache[i][j] = -1;
            }
        }
        return help(text1, text2, 0, 0);
    }
}
// @lc code=end

