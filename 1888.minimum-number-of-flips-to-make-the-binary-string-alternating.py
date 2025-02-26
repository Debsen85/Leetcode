#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#

# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        length = len(s)
        pattern1, pattern2 = [], []
        s = s + s

        for _ in range(len(s)):
            pattern1.append("0" if pattern1 and pattern1[-1] == "1" else "1")
            pattern2.append("1" if pattern2 and pattern2[-1] == "0" else "0")
        
        answer = length
        diff1, diff2 = 0, 0
        i, j = 0, 0

        while j < len(s):
            if s[j] != pattern1[j]:
                diff1 += 1

            if s[j] != pattern2[j]:
                diff2 += 1

            if j - i + 1 > length:
                if pattern1[i] != s[i]:
                    diff1 -= 1
                if pattern2[i] != s[i]:
                    diff2 -= 1
                i += 1
            if j - i + 1 == length:
                answer = min(answer, diff1, diff2)
            j += 1

        return answer
# @lc code=end

