/*
 * @lc app=leetcode id=695 lang=java
 *
 * [695] Max Area of Island
 */

// @lc code=start

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static int breadthFirstSearch(int[][] grid, int r, int c) {
        int area = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {r, c});
        grid[r][c] = 0;
        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            for (int[] dir: directions) {
                int dr = node[0] + dir[0], dc = node[1] + dir[1];
                if ((dr >= 0) && (dr < grid.length) && (dc >= 0) && (dc < grid[0].length) && grid[dr][dc] == 1) {
                    area ++;
                    grid[dr][dc] = 0;
                    queue.offer(new int[] {dr, dc});
                }
            }
        }
        return area;
    }

    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        for (int r = 0; r < grid.length; r ++) {
            for (int c = 0; c < grid[0].length; c ++) {
                if (grid[r][c] == 1) {
                    maxArea = Math.max(maxArea, breadthFirstSearch(grid, r, c));
                }
            }
        }
        return maxArea;
    }
}
// @lc code=end

