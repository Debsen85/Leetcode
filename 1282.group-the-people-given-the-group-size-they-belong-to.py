#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashMap = defaultdict(list)
        for index, group in enumerate(groupSizes):
            hashMap[group].append(index)
        hashMap = dict(sorted(hashMap.items()))
        answer = []
        for key in hashMap:
            if len(hashMap[key]) <= key:
                answer.append(hashMap[key])
            else:
                for right in range(0, len(hashMap[key]), key):
                    answer.append(hashMap[key][right : min(right + key, len(hashMap[key]))])
        return answer
# @lc code=end

