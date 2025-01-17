/*
 * @lc app=leetcode id=200 lang=java
 *
 * [200] Number of Islands
 */

// @lc code=start

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public static int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static void breadthFirstSearch(char[][] grid, int R, int C, int r, int c) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {r, c});
        grid[r][c] = '0';
        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            int row = node[0], col = node[1];
            for (int[] dir: directions) {
                int dr = row + dir[0], dc = col + dir[1];
                if ((dr >= 0) && (dr < R) && (dc >= 0) && (dc < C) && (grid[dr][dc] != '0')) {
                    queue.offer(new int[] {dr, dc});
                    grid[dr][dc] = '0';
                }
            }
        }
    }
    public int numIslands(char[][] grid) {
        int R = grid.length, C = grid[0].length, answer = 0;
        for (int r = 0; r < R; r ++) {
            for (int c = 0; c < C; c ++) {
                if (grid[r][c] == '1') {
                    breadthFirstSearch(grid, R, C, r, c);
                    answer ++;
                }
            }
        }
        return answer;
    }
}
// @lc code=end

