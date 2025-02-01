#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True if curr.word else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

