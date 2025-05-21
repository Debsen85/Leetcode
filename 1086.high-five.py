from collections import defaultdict
from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashMap = defaultdict(list)
        for id, score in items:
            hashMap[id].append(score)
        for key in hashMap:
            hashMap[key].sort(reverse=True)
        answer = []
        for key in hashMap:
            answer.append([key, sum(hashMap[key][:5]) // 5])
        return sorted(answer)