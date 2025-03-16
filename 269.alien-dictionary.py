#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjacentList = {c: set() for w in words for c in w}

        for i in range(1, len(words)):
            minLength = min(len(words[i]), len(words[i - 1]))
            if len(words[i]) < len(words[i - 1]) and words[i][:minLength] == words[i - 1][:minLength]:
                return ""
            for j in range(minLength):
                if words[i][j] != words[i - 1][j]:
                    adjacentList[words[i][j]].add(words[i - 1][j])
                    break

        visit = {}
        result = []

        def postorder(node):
            if node in visit:
                return visit[node]

            visit[node] = True
            for adj in adjacentList[node]:
                if postorder(adj):
                    return True
            visit[node] = False
            result.append(node)

        for adj in adjacentList:
            if postorder(adj):
                return ""

        return "".join(result)
# @lc code=end

