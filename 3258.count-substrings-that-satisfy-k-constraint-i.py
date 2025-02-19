#
# @lc app=leetcode id=3258 lang=python3
#
# [3258] Count Substrings That Satisfy K-Constraint I
#

# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        i, j = 0, 0
        counter = {}
        answer = 0
        while j < len(s):

            counter[s[j]] = counter.get(s[j], 0) + 1

            if counter.get('0', 0) <= k or counter.get('1', 0) <= k:
                answer += (j - i + 1)
                j += 1
            else:
                while counter.get('0', 0) > k and counter.get('1', 0) > k:
                    counter[s[i]] -= 1
                    i += 1
                answer += (j - i + 1)
                j += 1

        return answer        
# @lc code=end

