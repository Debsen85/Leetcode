/*
 * @lc app=leetcode id=994 lang=java
 *
 * [994] Rotting Oranges
 */

// @lc code=start

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    static int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static int breadthFirstSearch(int[][] grid, List<int[]> list) {
        int answer = 0;
        Queue<int[]> queue = new LinkedList<>();
        for (int[] pair: list) {
            queue.offer(pair);
        }
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i ++) {
                int node[] = queue.poll();
                for (int[] dir: directions) {
                    int dr = node[0] + dir[0], dc = node[1] + dir[1];
                    if (dr >= 0 && dr < grid.length && dc >= 0 && dc < grid[0].length && grid[dr][dc] == 1) {
                        queue.offer(new int[] {dr, dc});
                        grid[dr][dc] = 2;
                    }
                }
            }
            answer ++;
        }
        return answer - 1; 
    }

    public static boolean check(int[][] grid) {
        for (int r = 0; r < grid.length; r ++) {
            for (int c = 0; c < grid[0].length; c ++) {
                if (grid[r][c] == 1) {
                    return false;
                }
            }
        }
        return true;
    }

    public int orangesRotting(int[][] grid) {
        int answer = 0;
        if (check(grid)) {
            return 0;
        }
        List<int[]> list = new ArrayList<>();
        for (int r = 0; r < grid.length; r ++) {
            for (int c = 0; c < grid[0].length; c ++) {
                if (grid[r][c] == 2) {
                    list.add(new int[] {r, c});
                }
            }
        }
        answer = breadthFirstSearch(grid, list);
        if (check(grid)) {
            return answer;
        }   
        return -1;
    }
}
// @lc code=end

