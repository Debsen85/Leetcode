/*
 * @lc app=leetcode id=684 lang=java
 *
 * [684] Redundant Connection
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {

    Map<Integer, Integer> parent;
    Map<Integer, Integer> rank;

    public Solution() {
        this.parent = new HashMap<>();
        this.rank = new HashMap<>();
    }

    public int find(int x) {
        if (x != this.parent.get(x)) {
            this.parent.put(x, find(this.parent.get(x)));
        }
        return this.parent.get(x);
    }

    public boolean union(int x, int y) {
        x = find(x); 
        y = find(y);
        if (x == y) {
            return false;
        } else {
            if (this.rank.get(x) >= this.rank.get(y)) {
                this.parent.put(y, this.parent.get(x));
                this.rank.put(x, 1 + this.rank.get(y));
            } else {
                this.parent.put(x, this.parent.get(y));
                this.rank.put(y, 1 + this.rank.get(x));
            }
            return true;
        }
    }

    public int[] findRedundantConnection(int[][] edges) {
        int numberOfEdges = edges.length;
        
        for (int i = 1; i <= numberOfEdges; i ++) {
            this.parent.put(i, i);
            this.rank.put(i, 1);
        }

        for (int[] edge: edges) {
            if (!union(edge[0], edge[1])) {
                return edge;
            }
        }
        return new int[]{-1, -1};
    }
}
// @lc code=end

