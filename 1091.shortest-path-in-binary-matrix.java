/*
 * @lc app=leetcode id=1091 lang=java
 *
 * [1091] Shortest Path in Binary Matrix
 */

// @lc code=start

import java.util.LinkedList;
import java.util.Queue;

class Solution {

    static int[][] directions = {{-1, 0}, {-1, 1}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {0, 1}, {1, 1}};
    
    public int shortestPathBinaryMatrix(int[][] grid) {
        int answer = 1;
        if (grid[grid.length - 1][grid[0].length - 1] == 1 || grid[0][0] == 1) {
            return -1;
        }
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {0, 0});
        grid[0][0] = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i ++) {
                int []node = queue.poll();
                if (node[0] == grid.length - 1 && node[1] == grid[0].length - 1) {
                    return answer;
                }
                for (int[] dir : directions) {
                    int dr = dir[0] + node[0], dc = dir[1] + node[1];
                    if (dr < grid.length && dc < grid[0].length && dr >= 0 && dc >= 0 && grid[dr][dc] == 0) {
                        grid[dr][dc] = 1;
                        queue.offer(new int[] {dr, dc});
                    }
                }
            }
            answer ++;
        }
        return -1;
    }
}
// @lc code=end

