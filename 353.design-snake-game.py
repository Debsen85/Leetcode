#
# @lc app=leetcode id=353 lang=python3
#
# [353] Design Snake Game
#

# @lc code=start
import collections

class SnakeGame:
    def __init__(self, width,height,food):
        self.snake = collections.deque([[0,0]])
        self.width = width
        self.height = height
        self.food = collections.deque(food)
        self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        

    def move(self, direction):
        newHead = [self.snake[0][0]+self.direct[direction][0], self.snake[0][1]+self.direct[direction][1]]
        
        if (newHead[0] < 0 or newHead[0] >= self.height) or (newHead[1] < 0 or newHead[1] >= self.width)\
        or (newHead in self.snake and newHead != self.snake[-1]): return -1

        if self.food and self.food[0] == newHead:
            self.snake.appendleft(newHead)
            self.food.popleft()
        else:  
            self.snake.appendleft(newHead)   
            self.snake.pop()   
            
        return len(self.snake)-1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
# @lc code=end

