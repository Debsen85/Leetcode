/*
 * @lc app=leetcode id=978 lang=java
 *
 * [978] Longest Turbulent Subarray
 */

// @lc code=start
class Solution {
    public int maxTurbulenceSize(int[] arr) {
        if (arr.length == 1) {
            return arr.length;
        }
        int r = 2, total = 1, currTotal = 1, parity = 0;
        if (arr[0] > arr[1]) {
            parity = 1;
            currTotal = 2;
        } else if (arr[0] < arr[1]) {
            parity = -1;
            currTotal = 2;
        } else {
            parity = 0;
            currTotal = 1;
        }
        total = Math.max(currTotal, total);
        for (r = 2; r < arr.length; r ++) {
            if (arr[r - 1] > arr[r]) {
                if (parity == -1) {
                    currTotal ++;   
                } else {
                    currTotal = 2;
                }
                parity = 1;
            } else if (arr[r - 1] < arr[r]) {
                if (parity == 1) {
                    currTotal ++;   
                } else {
                    currTotal = 2;
                }
                parity = -1;
            } else {
                currTotal = 1;
                parity = 0;
            }
            total = Math.max(currTotal, total); 
        }
        return total;
    }
}
// @lc code=end

