#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#

# @lc code=start
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = ""
        stack = ['1']
        currentElement = 2
        for i in range(len(pattern)):
            if pattern[i] == 'I':
                while stack:
                    result += stack.pop()
            stack.append(str(currentElement))
            currentElement += 1
        while stack: 
            result += stack.pop()
        return result
        
# @lc code=end

