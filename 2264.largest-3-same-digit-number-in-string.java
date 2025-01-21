/*
 * @lc app=leetcode id=2264 lang=java
 *
 * [2264] Largest 3-Same-Digit Number in String
 */

// @lc code=start
class Solution {
    public String largestGoodInteger(String num) {
        String answer = "", curr = "";
        for (int i = 1; i < num.length() - 1; i ++) {
            char a = num.charAt(i - 1), b = num.charAt(i), c = num.charAt(i + 1);
            if (a == b && b == c) {
                curr = "" + a + b + c;
                if (answer.compareTo(curr) < 0) {
                    answer = curr;
                }
            }
        }
        return answer;
    }
}
// @lc code=end

