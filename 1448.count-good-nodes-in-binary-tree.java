/*
 * @lc app=leetcode id=1448 lang=java
 *
 * [1448] Count Good Nodes in Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public static int goodNode(TreeNode root, int maxVal) {
        if (root == null) {
            return 0;
        }
        int res = (root.val >= maxVal) ? 1 : 0;
        maxVal = Math.max(maxVal, root.val);
        res += goodNode(root.left, maxVal);
        res += goodNode(root.right, maxVal);

        return res;
    }

    public int goodNodes(TreeNode root) {
        return goodNode(root, root.val);
    }
}
// @lc code=end

