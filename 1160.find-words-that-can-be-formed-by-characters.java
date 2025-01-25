/*
 * @lc app=leetcode id=1160 lang=java
 *
 * [1160] Find Words That Can Be Formed by Characters
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countCharacters(String[] words, String chars) {
        Map<String, Integer> mapChars, mapWords;
        int answer = 0, i = 0;
        boolean flag = true;

        mapChars = new HashMap<>();
        for (i = 0; i < chars.length(); i ++) {
            char ch = chars.charAt(i);
            mapChars.put(String.valueOf(ch), mapChars.getOrDefault(String.valueOf(ch), 0) + 1);
        }

        for (String word: words) {
            mapWords = new HashMap<>();
            flag = true;
            for (i = 0; i < word.length(); i ++) {
                char ch = word.charAt(i);
                mapWords.put(String.valueOf(ch), mapWords.getOrDefault(String.valueOf(ch), 0) + 1);
            }
            for (String key: mapWords.keySet()) {
                if (mapChars.getOrDefault(key, 0) < mapWords.get(key)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                answer += word.length();
            }
        }
        return answer;
    }
}
// @lc code=end

