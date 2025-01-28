#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        temporary = set(wordList)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        

        def bfs():
            queue = deque()
            answer = 1
            queue.append(beginWord)

            while queue:
                for i in range(len(queue)):
                    word = queue.popleft()
                    if word == endWord:
                        return answer
                    for i in range(len(word)):
                        for ch in alphabet:
                            wordCheck = word[: i] + ch + word[i + 1 :]
                            if wordCheck in temporary:
                                queue.append(wordCheck)
                                temporary.remove(wordCheck)
                answer += 1
            return 0
        
        answer = []   
        small = [bfs()]
        temporary = set(wordList)
        if small[0] == 0:
            return []
        
        def dfs(result, length):
            if length > small[0]:
                return
            if result[-1] == endWord:
                if len(result) == small[0]:
                    answer.append(result[:])
                return
            
            word = result[-1]
            for i in range(len(word)):
                for ch in alphabet:
                    wordCheck = word[: i] + ch + word[i + 1 :]
                    if wordCheck in temporary:
                        result.append(wordCheck)
                        temporary.remove(wordCheck)
                        helper(result, length + 1)
                        result.pop()
                        temporary.add(wordCheck)
            
        dfs([beginWord], 1)
        return answer
# @lc code=end

