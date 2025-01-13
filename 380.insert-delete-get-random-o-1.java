/*
 * @lc app=leetcode id=380 lang=java
 *
 * [380] Insert Delete GetRandom O(1)
 */

// @lc code=start

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

class RandomizedSet {

    List<Integer> list;
    Map<Integer, Integer> map;
    Random random;

    public RandomizedSet() {
        this.list = new ArrayList<>();
        this.map = new HashMap<>();
        this.random = new Random();
    }
    
    public boolean insert(int val) {
        if (this.map.containsKey(val)) {
            return false;
        } else {
            this.list.add(val);
            this.map.put(val, this.list.size() - 1);
            return true;
        }
    }
    
    public boolean remove(int val) {
        if (!this.map.containsKey(val)) {
            return false;
        } else {
            int getIndex = this.map.get(val);
            int getLastElement = this.list.get(this.list.size() - 1);
            
            this.list.set(getIndex, getLastElement);
            this.map.put(getLastElement, getIndex);

            this.list.remove(this.list.size() - 1);
            this.map.remove(val);

            return true;
        }
    }
    
    public int getRandom() {
        return this.list.get(random.nextInt(this.list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
// @lc code=end

