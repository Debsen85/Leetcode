#
# @lc app=leetcode id=3039 lang=python3
#
# [3039] Apply Operations to Make String Empty
#

# @lc code=start
class Solution:
    def lastNonEmptyString(self, string: str) -> str:
        hashMap = {}
        for i, s in enumerate(string):
            if s not in hashMap:
                hashMap[s] = [1, i]
            else:
                hashMap[s][0] += 1
                hashMap[s][1] = i
        
        keys, values = list(hashMap.keys()), list(hashMap.values())

        m = max(values)
        result = []

        for key, value in zip(keys, values):
            if value[0] == m[0]:
                result.append(value[1])
        
        result.sort()
        answer = []

        for r in result:
            answer.append(string[r])

        return "".join(answer)
# @lc code=end

