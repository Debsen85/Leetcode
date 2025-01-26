#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        answer = ""
        open = 0
        close = 0

        for string in s:
            if string == '(':
                stack.append(string)
                open += 1
            elif string == ')':
                if len(stack):
                    inner = ""
                    while stack[-1] != '(':
                        inner = stack.pop() + inner
                    inner = stack.pop() + inner + string
                    if len(stack):
                        stack.append(inner)
                    else:
                        answer += inner
            else:
                if len(stack):
                    stack.append(string)
                else:
                    answer += string
        inner = ""
        while stack:
            if stack[-1] != '(':
                inner = stack.pop() + inner   
            else:
                stack.pop()
        answer += inner
        return answer
        
# @lc code=end

