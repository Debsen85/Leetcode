/*
 * @lc app=leetcode id=3375 lang=java
 *
 * [3375] Minimum Operations to Make Array Values Equal to K
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minOperations(int[] nums, int k) {
        int count = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int num: nums) {
            if (num < k) {
                return -1;
            }
            if (num != k) {
                if (!map.containsKey(num)) {
                    count ++;
                    map.put(num, 1);
                }
            }
        }
        return count;
    }
}
// @lc code=end

