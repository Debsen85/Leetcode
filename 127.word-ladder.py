#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
from typing import List

def difference(word1, word2):
    diff, length = 0, len(word1)
    for i in range(length):
        if word1[i] != word2[i]:
            diff += 1
        if diff > 1:
            return False
    return True

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = deque()
        visited = set()
        answer = 1
        queue.append(beginWord)
        visited.add(beginWord)

        while queue:
            #print(list(queue))
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return answer
                for wordCheck in wordList:
                    if difference(word, wordCheck) and wordCheck not in visited:
                        queue.append(wordCheck)
                        visited.add(wordCheck)
            answer += 1
        return 0
        
# @lc code=end

