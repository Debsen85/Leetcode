/*
 * @lc app=leetcode id=274 lang=java
 *
 * [274] H-Index
 */

// @lc code=start

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int hIndex(int[] citations) {
        int answer = 0, index = 1;
        List<Integer> list = new ArrayList<>();
        for (int c: citations) {
            list.add(c);
        }
        Collections.sort(list);
        for (int i = list.size() - 1; i >= 0; i --) {
            if (list.get(i) >= index) {
                answer ++;
                index ++;
            }
        }
        return answer;
    }
}
// @lc code=end

