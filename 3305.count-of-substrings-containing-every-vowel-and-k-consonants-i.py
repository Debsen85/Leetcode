#
# @lc app=leetcode id=3305 lang=python3
#
# [3305] Count of Substrings Containing Every Vowel and K Consonants I
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleast(k):
            answer = 0
            c, vMap = 0, defaultdict(int)
            i, j = 0, 0
            vowels = 'aeiou'
            while j < len(word):
                if word[j] in vowels:
                    vMap[word[j]] += 1
                else:
                    c += 1
                while len(vMap) == 5 and c >= k:
                    answer += len(word) - j
                    if word[i] in vowels:
                        vMap[word[i]] -= 1
                    else:
                        c -= 1
                    if vMap[word[i]] == 0:
                        vMap.pop(word[i])
                    i += 1 
                j += 1
            return answer
            
        return atleast(k) - atleast(k + 1) 
                
# @lc code=end

