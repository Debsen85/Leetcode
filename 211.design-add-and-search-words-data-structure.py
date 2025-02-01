#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.word = True

    def search(self, word: str) -> bool:
        def depthFirstSearch(root, letter):
            if letter == len(word):
                return root.word
            if word[letter] == ".":
                for value in root.children:
                    if depthFirstSearch(root.children[value], letter + 1):
                        return True
                return False
            if word[letter] not in root.children:
                return False
        
            return depthFirstSearch(root.children[word[letter]], letter + 1)

        return depthFirstSearch(self.trie, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

