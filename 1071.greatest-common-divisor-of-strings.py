#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prefix = []
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        n, m = len(str1), len(str2)
        string = ""
        
        for i in range(m):
            string += str2[i] 
            if n % (i + 1) == 0 and m % (i + 1) == 0:
                prefix.append(string)

        for p in prefix[::-1]:
            length = len(p)
            flag = True
            for i in range(0, n, length):
                if str1[i : i + length] != p :
                    flag = False
                    break
            for i in range(0, m, length):
                if str2[i : i + length] != p :
                    flag = False
                    break
            if flag:
                return p
        
        return ""
# @lc code=end

