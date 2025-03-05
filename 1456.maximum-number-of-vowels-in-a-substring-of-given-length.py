#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        total = 0
        answer = 0
        vowels = 'aeiou'
        i, j = 0, 0

        while j < len(s):
            if s[j] in vowels:
                total += 1

            if j - i + 1 > k:
                if s[i] in vowels:
                    total -= 1
                i += 1
            
            if j - i + 1 == k:
                answer = max(answer, total)
            
            j += 1
        
        return answer
# @lc code=end

