/*
 * @lc app=leetcode id=474 lang=java
 *
 * [474] Ones and Zeroes
 */

// @lc code=start
class Solution {
    int [][][] cache;

    public int findMaxForm(String[] strs, int m, int n) {
        this.cache = new int[strs.length][m + 1][n + 1];
        for (int i = 0; i < strs.length; i ++) {
            for (int j = 0; j < m + 1; j ++) {
                for (int k = 0; k < n + 1; k ++) {
                    this.cache[i][j][k] = 0;
                }
            }
        }
        return backtracking(0, strs, m, n);
    }

    public int count(String string, char ch) {
        int answer = 0;
        for (int i = 0; i < string.length(); i ++) {
            if (string.charAt(i) == ch) {
                answer ++;
            }
        }
        return answer;
    }

    public int backtracking(int index, String[] strs, int m, int n) {
        if (index == strs.length) {
            return 0;
        }
        if (cache[index][m][n] != 0) {
            return cache[index][m][n];
        }
        
        int M = count(strs[index], '0'), N = count(strs[index], '1');

        cache[index][m][n] = backtracking(index + 1, strs, m, n);

        if (m >= M && n >= N) {
            cache[index][m][n] = Math.max(cache[index][m][n], 1 + backtracking(index + 1, strs, m - M, n - N));
        }
        return cache[index][m][n];
    }
}
// @lc code=end

