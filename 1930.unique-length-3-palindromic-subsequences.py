#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        alphabetMap = defaultdict(int)
        indexMap = defaultdict(list)

        for i, letter in enumerate(s):
            alphabetMap[letter] += 1
            indexMap[letter].append(i)

        alphabetList = list(alphabetMap.values())
        alphabetKeys = list(alphabetMap.keys())

        if max(alphabetList) == 1:
            return 0

        answer = 0

        for i in range(len(alphabetList)):
            if alphabetList[i] >= 2:
                for j in range(len(alphabetList)):
                    if i == j:
                        if alphabetList[i] >= 3:
                            answer += 1
                    else:
                        for index in indexMap[alphabetKeys[j]]:
                            if indexMap[alphabetKeys[i]][0] < index < indexMap[alphabetKeys[i]][-1]:
                                answer += 1
                                break
        return answer
                    

        # @lc code=end

