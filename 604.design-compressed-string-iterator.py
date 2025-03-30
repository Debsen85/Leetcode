#
# @lc app=leetcode id=604 lang=python3
#
# [604] Design Compressed String Iterator
#

# @lc code=start
class StringIterator:

    def __init__(self, compressedString: str):
        self.string = self.uncompress(compressedString)
        self.index = 0

    def next(self) -> str:
        if self.index < len(self.string):
            self.index += 1
            return self.string[self.index - 1]
        return " "

    def hasNext(self) -> bool:
        return True if self.index < len(self.string) else False

    def uncompress(self, string):
        stack, digit = [], []
        for s in string:
            if s.isalpha():
                if stack:
                    stack[-1] = stack[-1] * int("".join(digit))
                stack.append(s)
                digit = []
            else:
                digit.append(s)
        if digit:
            stack[-1] = stack[-1] * int("".join(digit))
        return "".join(stack)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

