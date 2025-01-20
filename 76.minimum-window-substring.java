/*
 * @lc app=leetcode id=76 lang=java
 *
 * [76] Minimum Window Substring
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        if (s.equals("") || (s.length() < t.length())) {
            return "";
        }

        Map<Character, Integer> tMap = new HashMap<>();
        Map<Character, Integer> sMap = new HashMap<>();

        int need = 0, have = 0, minLen = Integer.MAX_VALUE, i = 0, j = 0;
        int[] answer = {-1, -1};

        for (i = 0; i < t.length(); i ++) {
            tMap.put(t.charAt(i), tMap.getOrDefault(t.charAt(i), 0) + 1);
        }

        need = tMap.size();
        i = 0;

        while (j < s.length()) {
            char currentCharacter = s.charAt(j);
            sMap.put(currentCharacter, sMap.getOrDefault(currentCharacter, 0) + 1);
            if (tMap.containsKey(currentCharacter) && sMap.get(currentCharacter).equals(tMap.getOrDefault(currentCharacter, 0))) {
                have ++;
            }
            while (have >= need) {
                if (minLen > j - i + 1) {
                    minLen = j - i + 1;
                    answer[0] = i;
                    answer[1] = j + 1; 
                }
                char leftChar = s.charAt(i);
                i ++;
                sMap.put(leftChar, sMap.get(leftChar) - 1);
                if (tMap.containsKey(leftChar) && sMap.get(leftChar) < tMap.getOrDefault(leftChar, 0)) {
                    have --;
                }
            }
            j ++;
        }
        return minLen == Integer.MAX_VALUE ? "" : s.substring(answer[0], answer[1]);
    }
}
// @lc code=end

