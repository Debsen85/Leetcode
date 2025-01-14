/*
 * @lc app=leetcode id=102 lang=java
 *
 * [102] Binary Tree Level Order Traversal
 */

// @lc code=start

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        Deque<TreeNode> deque = new ArrayDeque<>();
        List<List<Integer>> list = new ArrayList<>();
        deque.addLast(root);
        while(deque.size() > 0) {
            List<Integer> innerList = new ArrayList<>();
            int size = deque.size();
            for (int i = 1; i <= size; i ++) {
                TreeNode node = deque.removeFirst();
                innerList.add(node.val);
                if (node.left != null) {
                    deque.addLast(node.left);
                } 
                if (node.right != null) {
                    deque.addLast(node.right);
                }           
            }
            list.add(innerList);
        }
        return list;
    }
}
// @lc code=end

