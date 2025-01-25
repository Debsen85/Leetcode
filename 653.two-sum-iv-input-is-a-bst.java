/*
 * @lc app=leetcode id=653 lang=java
 *
 * [653] Two Sum IV - Input is a BST
 */

// @lc code=start

import java.util.HashSet;
import java.util.Set;

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
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> set = new HashSet<>();
        return helper(root, k, set);
    }

    public boolean helper(TreeNode root, int k, Set<Integer> set) {
        if (root == null) {
            return false;
        }

        if (set.contains(root.val)) {
            return true;
        }

        set.add(k - root.val);

        return helper(root.left, k, set) || helper(root.right, k, set);
    }
}
// @lc code=end

