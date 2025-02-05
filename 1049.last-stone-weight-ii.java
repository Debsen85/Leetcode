/*
 * @lc app=leetcode id=1049 lang=java
 *
 * [1049] Last Stone Weight II
 */

// @lc code=start
class Solution {
    int sum = 0, target = 0;
    int[][] cache;

    public int lastStoneWeightII(int[] stones) {
        for (int stone: stones) this.sum += stone;
        this.target = (this.sum + 1) / 2;
        cache = new int[stones.length][target + 1];
        for (int i = 0; i < stones.length; i ++) {
            for (int j = 0; j < target + 1; j ++) {
                cache[i][j] = Integer.MAX_VALUE;
            }
        }
        return backtracking(0, stones, 0, this.target, this.sum);
    }

    public int backtracking(int index, int[] stones, int total, int target, int sum) {
        if (index == stones.length || total >= target) {
            return Math.abs(total - (sum - total));
        }
        if (cache[index][total] != Integer.MAX_VALUE) {
            return cache[index][total];
        }
        cache[index][total] = Math.min(backtracking(index + 1, stones, total, target, sum), backtracking(index + 1, stones, total + stones[index], target, sum));
        return cache[index][total];
    }
}
// @lc code=end

