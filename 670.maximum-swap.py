#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        stringNum = str(num)
        stringList = list(stringNum)
        nextGreater = [[-1] * 2 for _ in range(len(stringList))]
        stack = []
        stack.append((stringList[-1], len(stringList) - 1))

        for i in reversed(range(len(stringList) - 1)):
            if stringList[i] > stack[-1][0]:
                stack.pop()
                stack.append((stringList[i], i))

            elif stringList[i] < stack[-1][0]:
                nextGreater[i][0] = stack[-1][0]
                nextGreater[i][1] = stack[-1][1]

        print(nextGreater, stack, stringList)

        for i in range(len(stringList)):
            if nextGreater[i][0] != -1:
                stringList[i], stringList[nextGreater[i][1]] = stringList[nextGreater[i][1]], stringList[i]
                break
            
        return int(''.join(stringList))
# @lc code=end

