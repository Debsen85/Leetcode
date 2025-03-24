#
# @lc app=leetcode id=1682 lang=python3
#
# [1682] Longest Palindromic Subsequence II
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.answer = 0

        def check(array):
            if len(array) % 2: return False
            m = len(array) // 2
            for i in range(1, len(array)):
                a, b = i - 1, i
                if b == m and a == m - 1:
                    continue
                if array[a] == array[b]:
                    return False
            return "".join(array) == "".join(array)[::-1]

        def backtracking(index, string):
            if index == len(s):
                if string and check(string[:]):
                    self.answer = max(self.answer, len(string))
                return

            string.append(s[index])
            backtracking(index + 1, string)
            string.pop()
            backtracking(index + 1, string)

        backtracking(0, [])
        return self.answer
# @lc code=end

