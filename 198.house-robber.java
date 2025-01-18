/*
 * @lc app=leetcode id=198 lang=java
 *
 * [198] House Robber
 */

// @lc code=start

class Solution {

    public int rob(int[] nums) {
        int rob1 = 0, rob2 = 0;
        for (int num : nums) {
            int temp = Math.max(rob1 + num, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        return rob2;
    }
}
// @lc code=end

