#
# @lc app=leetcode id=3304 lang=python3
#
# [3304] Find the K-th Character in String Game I
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:
        string = "a"
        while True:
            dummy = ""
            for s in string:
                if s == 'z':
                    dummy += 'a'
                else :
                    dummy += chr(ord(s) + 1)
            string += dummy
            if len(string) >= k:
                break
        return string[k - 1]
# @lc code=end

