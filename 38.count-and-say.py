#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        answer = ["1"]
        while (n - 1):
            n -= 1
            current = []
            c = 1
            v = answer[0]
            for i in range(1, len(answer)):
                if v != answer[i]:
                    current.append(str(c))
                    current.append(str(v))
                    c = 1
                    v = answer[i]
                else:
                    c += 1
            current.append(str(c))
            current.append(str(v))
            if current:
                answer = current[:]
        return "".join(answer)

# @lc code=end

