#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        num1 = list(num1)[::-1]
        num2 = list(num2)

        answer, c, zero = [], 0, len(num2) - 1

        for num in num2:
            number = []
            c = 0
            for n in num1:
                d = int(n) * int(num) + c
                c = d // 10
                number.append(str(d % 10))
    
            if (c > 0):
                number.append(str(c))

            number = "".join(number)
            for _ in range(zero):
                number = "0" + number
            answer.append(list(number))
            zero -= 1

        for i in range(1, len(answer)):
            answer[i] = answer[i] + (["0"] * (len(answer[0]) - len(answer[i])))
        
        c, d, result = 0, 0, []
        for i in range(len(answer[0])):
            d = 0
            for j in range(len(answer)):
                d += int(answer[j][i])
            d += c
            c = d // 10
            result.append(str(d % 10))
        if c > 0:
            result.append(str(c))

        return "".join(result[::-1])
# @lc code=end

