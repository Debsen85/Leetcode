/*
 * @lc app=leetcode id=983 lang=java
 *
 * [983] Minimum Cost For Tickets
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    int [] cache;
    public int mincostTickets(int[] days, int[] costs) {
        cache = new int[days.length + 1];
        Arrays.fill(cache, Integer.MAX_VALUE);
        return backtracking(0, days.length, days, costs);
    }

    public int backtracking(int index, int length, int[] days, int[] costs) {
        if (index == length) {
            return 0;
        }

        if (cache[index] != Integer.MAX_VALUE) {
            return cache[index];
        }

        cache[index] = Integer.MAX_VALUE;
        int i = 0, j = index;
        for (int day: new int[]{1, 7, 30}) {
            while (j < length && days[j] < days[index] + day) {
                j ++;
            }
            cache[index] = Math.min(cache[index], costs[i] + backtracking(j, length, days, costs));
            i ++;
        }
        return cache[index];
    }
}
// @lc code=end

