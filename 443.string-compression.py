#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 1
        count = 1
        char = chars[0]
        while j < len(chars):
            if chars[j] != char:
                if count == 1:
                    i += 1
                else:
                    i += 1
                    stringCount = str(count)
                    k = 0
                    while k < len(stringCount):
                        chars[i] = stringCount[k]
                        i += 1
                        k += 1
                char = chars[j]
                chars[i] = chars[j]
                count = 1
            else:
                count += 1
            j += 1
        if count == 1:
            i += 1
        else:
            i += 1
            stringCount = str(count)
            k = 0
            while k < len(stringCount):
                chars[i] = stringCount[k]
                i += 1
                k += 1
        return i
# @lc code=end

