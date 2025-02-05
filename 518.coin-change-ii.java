/*
 * @lc app=leetcode id=518 lang=java
 *
 * [518] Coin Change II
 */

// @lc code=start
class Solution {
    int [][] cache;
    public int change(int amount, int[] coins) {
        cache = new int[coins.length][amount + 1];
        for (int i = 0; i < coins.length; i ++) {
            for (int j = 0; j < amount + 1; j ++) {
                cache[i][j] = -1;
            }
        }
        return backtracking(0, amount, coins);
    }
    public int backtracking(int index, int amount, int[] coins) {
        if (amount == 0) {
            return 1;
        }
        if (amount < 0 || index == coins.length) {
            return 0;
        }
        if (cache[index][amount] != -1) {
            return cache[index][amount];
        }
        cache[index][amount] = backtracking(index + 1, amount, coins) + backtracking(index, amount - coins[index], coins);
        return cache[index][amount];
    }
}
// @lc code=end

