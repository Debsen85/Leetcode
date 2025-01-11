/*
 * @lc app=leetcode id=912 lang=java
 *
 * [912] Sort an Array
 */

// @lc code=start
class Solution {
    public static void merge(int[] nums, int s, int m, int e) {
        int[] L = new int[m - s + 1];
        int[] R = new int[e - m];
        int i, j, k; 
        for (i = 0; i < m - s + 1; i ++) {
            L[i] = nums[s + i];
        }
        for (j = 0; j < e - m; j ++) {
            R[j] = nums[m + 1 + j];
        }
        k = s;
        i = 0;
        j = 0;
        while (i < L.length && j < R.length) {
            if (L[i] <= R[j]) {
                nums[k] = L[i];
                i ++;
            } else {
                nums[k] = R[j];
                j ++;
            }
            k ++;
        }
        while (i < L.length) {
            nums[k] = L[i];
            k ++;
            i ++;
        }
        while (j < R.length) {
            nums[k] = R[j];
            k ++;
            j ++;
        }
    }

    public static void mergeSort(int[] nums, int s, int e) {
        if (s < e) {
            int m = (e + s) / 2;

            mergeSort(nums, s, m);
            mergeSort(nums, m + 1, e);
            merge(nums, s, m, e);
        }
    }

    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }
}
// @lc code=end

