/*
 * @lc app=leetcode id=146 lang=java
 *
 * [146] LRU Cache
 */

// @lc code=start

import java.util.LinkedHashMap;
import java.util.Map;

class LRUCache {

    Map<Integer, Integer> map;
    int capacity;
    
    public LRUCache(int capacity) {
        this.map = new LinkedHashMap<>(capacity, 0.75f, true) {
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > LRUCache.this.capacity;
            }
        };
        this.capacity = capacity;
    }
    
    public int get(int key) {
        return this.map.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        this.map.put(key, value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end

