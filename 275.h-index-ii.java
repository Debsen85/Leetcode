/*
 * @lc app=leetcode id=275 lang=java
 *
 * [275] H-Index II
 */

// @lc code=start
class Solution {
    public int hIndex(int[] citations) {
        int l = 0, r = citations.length - 1, m = 0, res = 0;

        while (l <= r) {

            m = (l + r) / 2;

            if (citations[m] >= citations.length - m) {
                System.out.println("First");
                res = m;
                if (m == 0) {
                    return citations.length;
                } else if (m == citations.length - 1) {
                    return 1;
                }
                r = m - 1;
            } else {
                System.out.println("Second");
                if (m == 0 && citations.length == 1 || m == citations.length - 1) {
                    return 0;
                }
                l = m + 1;
            }
        }
        return citations.length - res;
    }
}
// @lc code=end

