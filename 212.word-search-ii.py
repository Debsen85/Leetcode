#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.trie = TrieNode()

    def depthFirstSearch(self, curr, i, j, board, visited, length):
        if length == 10:
            return 
        if min(i, j) < 0 or i == len(board) or j == len(board[0]) or (i, j) in visited:
            return
        if board[i][j] not in curr.children:
            curr.children[board[i][j]] = TrieNode()
        visited.add((i, j))

        self.depthFirstSearch(curr.children[board[i][j]], i + 1, j, board, visited, length + 1)
        self.depthFirstSearch(curr.children[board[i][j]], i - 1, j, board, visited, length + 1)
        self.depthFirstSearch(curr.children[board[i][j]], i, j + 1, board, visited, length + 1)
        self.depthFirstSearch(curr.children[board[i][j]], i, j - 1, board, visited, length + 1)

        visited.remove((i, j))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.depthFirstSearch(self.trie, i, j, board, set(), 0)
        
        answer = set()
        for word in words:
            curr = self.trie
            flag = True
            for letter in word:
                if letter not in curr.children:
                    flag = False
                    break
                curr = curr.children[letter]
            if flag:
                answer.add(word)
        
        return list(answer)
        
# @lc code=end

