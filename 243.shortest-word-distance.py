class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        l, r, d, t = 0, 0, float("inf"), -1
        while r < len(wordsDict):
            if t == -1:
                while r < len(wordsDict) and wordsDict[r] not in [word1, word2]:
                    r += 1
                if wordsDict[r] == word1:
                    t = 1
                else:
                    t = 2
                l = r
            elif t == 1:
                while r < len(wordsDict) and wordsDict[r] not in [word1, word2]:
                    r += 1
                if r < len(wordsDict) and wordsDict[r] == word2:
                    d = min(d, r - l)
                    t = 2
                l = r
            else:
                while r < len(wordsDict) and wordsDict[r] not in [word1, word2]:
                    r += 1
                if r < len(wordsDict) and wordsDict[r] == word1:
                    d = min(d, r - l)
                    t = 1
                l = r
            r += 1
            print(d)
        return d
