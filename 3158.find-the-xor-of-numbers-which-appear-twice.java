/*
 * @lc app=leetcode id=3158 lang=java
 *
 * [3158] Find the XOR of Numbers Which Appear Twice
 */

// @lc code=start

import java.util.Arrays;
import java.util.function.Function;
import java.util.stream.Collectors;

class Solution {
    public int duplicateNumbersXOR(int[] nums) {
        return Arrays.stream(nums).boxed().collect(Collectors.groupingBy(Function.identity(), Collectors.counting())).entrySet().stream().filter(x -> x.getValue() == 2).map(x -> x.getKey()).collect(Collectors.toList()).stream().reduce(0, (x, y) -> x ^ y);
    }
}
// @lc code=end

