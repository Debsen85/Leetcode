/*
 * @lc app=leetcode id=118 lang=java
 *
 * [118] Pascal's Triangle
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> list = new ArrayList<>();
        List<Integer> innerList = new ArrayList<>();
        List<Integer> prevList = new ArrayList<>();
        innerList.add(1);
        list.add(innerList);
        if (numRows == 1) { 
            return list;
        } 
        innerList = new ArrayList<>();
        innerList.add(1);
        innerList.add(1);
        list.add(innerList);
        if (numRows == 2) {
            return list;
        }
        for (int i = 0; i < numRows - 2; i ++) {
            prevList = innerList;
            innerList = new ArrayList<>();
            innerList.add(1);
            for (int j = 0; j < prevList.size() - 1; j ++) {
                innerList.add(prevList.get(j) + prevList.get(j + 1));
            }
            innerList.add(1);
            list.add(innerList);
        }
        return list;
    }
}
// @lc code=end

