#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.wordMap = {}
        for index, word in enumerate(words):
            for i in range(len(word)):
                pref = word[ : i + 1]
                for j in range(len(word)):
                    curr = pref + "@" + word[j : ]
                    self.wordMap[curr] = index

    def f(self, pref: str, suff: str) -> int:
        word = pref + "@" + suff
        if word not in self.wordMap:
            return -1
        return self.wordMap[word]
 

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# @lc code=end

