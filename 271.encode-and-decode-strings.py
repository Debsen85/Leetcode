#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        return '//3//'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        return s.split('//3//')
        

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end

