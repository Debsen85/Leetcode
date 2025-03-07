#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        binA, binB, binC = bin(a)[2 : ], bin(b)[2 : ], bin(c)[2 : ]
        length = max(len(binA), len(binB), len(binC))

        binA = "0" * (length - len(binA)) + binA
        binB = "0" * (length - len(binB)) + binB
        binC = "0" * (length - len(binC)) + binC

        answer = 0

        for i in range(length):
            if (binA[i] == '1' and binB[i] == '1') and binC[i] == '0':
                answer += 2
            elif (binA[i] == '1' or binB[i] == '1') and binC[i] == '0':
                answer += 1
            elif (binA[i] == '0' and binB[i] == '0') and binC[i] == '1':
                answer += 1
        
        return answer
# @lc code=end

