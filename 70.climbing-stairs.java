/*
 * @lc app=leetcode id=70 lang=java
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
    public int climbStairs(int n) {
        int[] dp = {1, 2};
        if (n <= 2) {
            return n;
        }
        int i = 3;
        while (n >= i) {
            int temp = dp[1];
            dp[1] = dp[0] + dp[1];
            dp[0] = temp;
            i ++;
        }
        return dp[1];
    }
}
// @lc code=end

