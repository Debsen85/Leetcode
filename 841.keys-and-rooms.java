/*
 * @lc app=leetcode id=841 lang=java
 *
 * [841] Keys and Rooms
 */

// @lc code=start

import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.concurrent.ConcurrentLinkedQueue;

class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visited = new HashSet<>();
        Queue<List<Integer>> queue = new ConcurrentLinkedQueue<>();
        visited.add(0);
        queue.offer(rooms.get(0));
        while (!queue.isEmpty()) {
            for (List<Integer> nodes: queue) {
                for (Integer node: nodes) {
                    if (!visited.contains(node)) {
                        visited.add(node);
                        queue.offer(rooms.get(node));
                    }
                }
                queue.poll();
            }
        }

        return visited.size() == rooms.size();
    }
}
// @lc code=end

