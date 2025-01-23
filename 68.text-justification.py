#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        innerList = []
        answerList = []
        currString = ""
        length = 0
        space = 0
        spaceLength = 0
        spaceReminder = 0
        words = deque(words)

        while words:
            val = words.popleft()
            innerList.append(val)
            length += len(val)

            total = length + len(innerList) - 1            
    
            if total >= maxWidth:
                val = None
                if total > maxWidth:
                    val = innerList.pop()
                    length -= len(val)
                    words.appendleft(val)
                
                space = maxWidth - length
                spaceLength = space // (len(innerList) - 1) if len(innerList) > 1 else 1

                if len(innerList) == 1:
                    currString = innerList[0] + (" " * (maxWidth - len(innerList[0])))

                elif space % (len(innerList) - 1) == 0:
                    for j in range(len(innerList)):
                        currString += innerList[j]
                        
                        if j < len(innerList) - 1:
                            currString += (" " * spaceLength)
                
                else:
                    spaceReminder = space % (len(innerList) - 1)
                    for j in range(len(innerList)):
                        currString += innerList[j]
                        
                        if j < len(innerList) - 1:
                            if j < spaceReminder:
                                currString += (" " * (spaceLength + 1))
                            else:
                                currString += (" " * (spaceLength))
                
                answerList.append(currString)
                innerList = []
                length = 0
                currString = ""

        print(innerList, list(words), length)
        if innerList:
            if len(innerList) == 1:
                currString = innerList[0] + (" " * (maxWidth - len(innerList[0])))
            else:                
                space = maxWidth - length - (len(innerList) - 1)
                for j in range(len(innerList)):
                    currString += innerList[j]
                    
                    if j < len(innerList) - 1:
                        currString += " "
                currString += (" " * space)
            answerList.append(currString)

        return answerList
                
# @lc code=end

