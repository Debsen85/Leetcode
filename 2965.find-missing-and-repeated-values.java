/*
 * @lc app=leetcode id=2965 lang=java
 *
 * [2965] Find Missing and Repeated Values
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        Map<Integer, Integer> map = new HashMap<>();
        int n = grid.length;
        int actualSum = ((n * n) * ((n * n) + 1)) / 2;
        int sum = 0;
        int [] answer = new int[2];

        for(int r = 0; r < n; r ++) {
            for(int c = 0; c < n; c ++) {
                map.put(grid[r][c], map.getOrDefault(grid[r][c], 0) + 1);
                sum += grid[r][c];
            }
        }

        for (int key : map.keySet()) {
            if (map.get(key) == 2) {
                answer[0] = key;
                answer[1] = actualSum - (sum - key);
                return answer;
            }
        }
        return answer;
    }
}
// @lc code=end

