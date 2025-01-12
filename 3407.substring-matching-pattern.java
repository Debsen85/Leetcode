/*
 * @lc app=leetcode id=3407 lang=java
 *
 * [3407] Substring Matching Pattern
 */

// @lc code=start
class Solution {
    public boolean hasMatch(String s, String p) {
        int ind = p.indexOf("*");
        if (p.length() == 1) {
            return true;
        }
        if (ind == 0) {
            p = p.substring(1, p.length());
            if (s.indexOf(p) != -1) {
                return true;
            } else {
                return false;
            }
        } else if (ind == p.length() - 1) {
            p = p.substring(0, p.length() - 1);
            if (s.indexOf(p) != -1) {
                return true;
            } else {
                return false;
            }
        } else {
            String a = p.substring(0, ind), b = p.substring(ind + 1, p.length());
            if ((s.indexOf(a) != -1) && (s.substring(s.indexOf(a) + a.length(), s.length()).indexOf(b) != -1)) {
                return true;
            } else {
                return false;
            }
        }
    }
}
// @lc code=end