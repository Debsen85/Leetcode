/*
 * @lc app=leetcode id=122 lang=java
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int answer = 0;

        for (int i = 0; i < prices.length - 1; i ++) {
            if (prices[i + 1] - prices[i] > 0) {
                answer += prices[i + 1] - prices[i];
            }
        }
        return answer;
    }
}
// @lc code=end

