#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, 0
        w, b = 0, 0
        answer = len(blocks)
        while r < len(blocks):
            if blocks[r] == 'W':
                w += 1
            else:
                b += 1
            
            if r - l + 1 > k:
                if blocks[l] == 'W':
                    w -= 1
                else:
                    b -= 1
                l += 1
            
            if r - l + 1 == k:
                answer = min(answer, w)
            r += 1
        return answer
# @lc code=end

