#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        check = set()
        values = "abc"
        times = [k]
        answer = []

        def backtracking(index, permutations, prev):
            if times[0] == 0:
                return
            if index == n:
                string = "".join(permutations[:])
                if len(permutations) == n:
                    check.add(string)
                    times[0] -= 1
                    if times[0] == 0:
                        answer.append(string)
                return
            for value in values:
                if prev != value:
                    permutations.append(value)
                    backtracking(index + 1, permutations, value)
                    permutations.pop()

        backtracking(0, [], "")
        return answer[0] if answer else ""
# @lc code=end

