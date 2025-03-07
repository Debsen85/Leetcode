#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, string: str) -> str:
        stack = []

        for s in string: # type: ignore
            if s == "]":

                current = ""
                number = ""

                while stack[-1].isalpha():
                    current = stack.pop() + current

                stack.pop()

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number


                stack.append(current * int(number))
                
            else:
                stack.append(s)

        return "".join(stack)
# @lc code=end

