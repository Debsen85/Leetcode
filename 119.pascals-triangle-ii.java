/*
 * @lc app=leetcode id=119 lang=java
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> innerList = new ArrayList<>();
        List<Integer> prevList = new ArrayList<>();
        innerList.add(1);
        if (rowIndex == 0) { 
            return innerList;
        } 
        innerList = new ArrayList<>();
        innerList.add(1);
        innerList.add(1);
        if (rowIndex == 1) {
            return innerList;
        }
        for (int i = 0; i < rowIndex - 1; i ++) {
            prevList = innerList;
            innerList = new ArrayList<>();
            innerList.add(1);
            for (int j = 0; j < prevList.size() - 1; j ++) {
                innerList.add(prevList.get(j) + prevList.get(j + 1));
            }
            innerList.add(1);
        }
        return innerList;
    }
}
// @lc code=end

