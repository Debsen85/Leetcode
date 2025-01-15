/*
 * @lc app=leetcode id=199 lang=java
 *
 * [199] Binary Tree Right Side View
 */

// @lc code=start

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

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
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        Queue<TreeNode> queue = new LinkedList<>();
        List<Integer> list = new ArrayList<>();
        list.add(root.val);
        queue.add(root);
        while (queue.size() > 0) {
            int size = queue.size();
            int rightMost = 0;
            for (int i = 0; i < size; i ++) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    rightMost = node.left.val;
                    queue.add(node.left);
                }
                if (node.right != null) {
                    rightMost = node.right.val;
                    queue.add(node.right);
                }
            }
            if (queue.size() > 0) {
                list.add(rightMost);
            }
        }
        return list;
    }
}
// @lc code=end

