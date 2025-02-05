/*
 * @lc app=leetcode id=1790 lang=java
 *
 * [1790] Check if One String Swap Can Make Strings Equal
 */

// @lc code=start
class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int diff = 0;
        char c1 = ' ', c2 = ' ';
        for (int index = 0; index < s1.length(); index ++) {
            if (s1.charAt(index) != s2.charAt(index)) {
                diff ++;
                if (diff == 1) {
                    c1 = s1.charAt(index);
                    c2 = s2.charAt(index);
                } else if (diff == 2) {
                    if (s1.charAt(index) != c2 || s2.charAt(index) != c1) {
                        return false;
                    }
                }
            }
            if (diff > 2) {
                return false;
            }
        }
        return diff == 2 ? true : diff == 0 ? true : false;
    }
}
// @lc code=end

