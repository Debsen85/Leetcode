/*
 * @lc app=leetcode id=2306 lang=java
 *
 * [2306] Naming a Company
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long distinctNames(String[] ideas) {
        long answer = 0;
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < ideas.length; i ++) {
            map.put(ideas[i], map.getOrDefault(ideas[i], 0) + 1);
        }

        for (int i = 0; i < ideas.length - 1; i ++) {
            for (int j = i + 1; j < ideas.length; j ++) {
                String a = ideas[i].substring(0, 1) + ideas[j].substring(1);
                String b = ideas[j].substring(0, 1) + ideas[i].substring(1);

                if (!(map.containsKey(a) || map.containsKey(b))) {
                    answer += 1;
                }
            }
        }
        return answer * 2;
    }
}
// @lc code=end

