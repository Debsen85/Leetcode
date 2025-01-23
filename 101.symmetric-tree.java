/*
 * @lc app=leetcode id=101 lang=java
 *
 * [101] Symmetric Tree
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
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        List<Integer> list = new ArrayList<>();
        while (!queue.isEmpty()) {
            int size = queue.size();
            list = new ArrayList<>();
            for (int i = 0; i < size; i ++) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    list.add(node.left.val);
                    queue.offer(node.left);
                } else {
                    list.add(1000);
                }
                if (node.right != null) {
                    list.add(node.right.val);
                    queue.offer(node.right);
                } else {
                    list.add(1000);
                }
            }
            int l = 0, r = list.size() - 1;
            while (l <= r) {
                if (!list.get(l).equals(list.get(r))) {
                    return false;
                }
                l ++;
                r --;
            }
        }
        return true;
    }
}
// @lc code=end

