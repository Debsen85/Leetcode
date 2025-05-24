#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#

# @lc code=start
class Solution(object):
    def findWordsContaining(self, words, x):
        Ind = []
        for i in range(len(words)):
            if x in words[i]:
                Ind.append(i)
        return Ind
        
        
# @lc code=end

