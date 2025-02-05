/*
 * @lc app=leetcode id=322 lang=java
 *
 * [322] Coin Change
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    Map<Integer, Integer> cache = new HashMap<>();
    public int coinChange(int[] coins, int amount) {
        int answer =  backtracking(coins, amount);  
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
    public int backtracking(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }
        if (cache.containsKey(amount)) {
            return cache.get(amount);
        }
        int result = Integer.MAX_VALUE;
        for(int coin : coins) {
            if (amount - coin >= 0) {
                int minimumCost = backtracking(coins, amount - coin);
                if (minimumCost != Integer.MAX_VALUE) {
                    result = Math.min(minimumCost + 1, result);
                }
            }
        }
        cache.put(amount, result);
        return cache.get(amount);
    }
}
// @lc code=end

