class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        state = list(currentState)
        answer = []
        for index in range(1, len(currentState)):
            if currentState[index] == currentState[index - 1]:
                if currentState[index] == '+':
                    answer.append("".join(currentState[ : index - 1]) + '--' + "".join(currentState[index + 1 : ]))
        return answer