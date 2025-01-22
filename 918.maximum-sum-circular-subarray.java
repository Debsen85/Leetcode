/*
 * @lc app=leetcode id=918 lang=java
 *
 * [918] Maximum Sum Circular Subarray
 */

// @lc code=start
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int sum = 0, minSum = Integer.MAX_VALUE, currMin = 0, maxSum = Integer.MIN_VALUE, currMax = 0;
        for (int num: nums) {
            if (currMin >= 0) {
                currMin = num;
            } else {
                currMin += num;
            }
            if (currMax <= 0) {
                currMax = num;
            } else {
                currMax += num;
            }
            minSum = Math.min(minSum, currMin);
            maxSum = Math.max(maxSum, currMax);
            sum += num;
        }
        return Math.max(maxSum, (sum - minSum == 0) ? maxSum : sum - minSum);
    }
}
// @lc code=end

