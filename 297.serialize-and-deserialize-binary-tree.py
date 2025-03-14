#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        def serial(node):
            if node:
                values.append(str(node.val))
                serial(node.left)
                serial(node.right)
            else:
                values.append('#')
        values = []
        serial(root)
        return ' '.join(values)

    def deserialize(self, data):
        def deserial():
            value = next(values)
            if value == '#':
                return None
            node = TreeNode(int(value))
            node.left = deserial()
            node.right = deserial()
            return node
        values = iter(data.split())
        return deserial()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

