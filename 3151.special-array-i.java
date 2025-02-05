/*
 * @lc app=leetcode id=3151 lang=java
 *
 * [3151] Special Array I
 */

// @lc code=start
class Solution {
    public boolean isArraySpecial(int[] nums) {
        if (nums.length == 1) {
            return true;
        }
        int parity = nums[0] % 2 == 1 ? 1 : 0;
        for (int index = 1; index < nums.length; index ++) {
            if (nums[index] % 2 == 0) {
                if (parity == 0) {
                    return false;
                } 
                parity = 0;
            } else {
                if (parity == 1) {
                    return false;
                }
                parity = 1;
            }
        }
        return true;
    }
}
// @lc code=end

