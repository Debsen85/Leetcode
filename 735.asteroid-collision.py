#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            flag = True
            while stack and stack[-1] > 0 and asteroid < 0: 
                if abs(stack[-1]) > abs(asteroid):
                    flag = False
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    stack.pop()
                    flag= False
                    break
            if flag:
                stack.append(asteroid)
            
        return stack
# @lc code=end

