/*
 * @lc app=leetcode id=554 lang=java
 *
 * [554] Brick Wall
 */

// @lc code=start

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        int prefix = 0, max = 0;
        Map<Integer, Integer> mapWall = new HashMap<>();

        for (int i = 0; i < wall.size(); i ++) {
            prefix = 0;
            for (int j = 0; j < wall.get(i).size(); j ++) {
                prefix += wall.get(i).get(j);
                mapWall.put(prefix, mapWall.getOrDefault(prefix, 0) + 1);
            }
        }

        for (int key: mapWall.keySet()) {
            if (key < prefix) {
                max = Math.max(max, mapWall.get(key));
            }
        }

        System.out.println(mapWall);

        return wall.size() - max;
    }
}
// @lc code=end

