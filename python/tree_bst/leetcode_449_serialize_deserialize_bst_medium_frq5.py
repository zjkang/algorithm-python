"""
author: Zhengjian Kang
date: 10/09/2020

https://leetcode.com/problems/serialize-and-deserialize-bst/

449. Serialize and Deserialize BST

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
"""


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        s = []
        self._encode(root, s)
        return ",".join(s)

    def _encode(self, root, s):
        if not root:
            return
        s.append(str(root.val))
        self._encode(root.left, s)
        self._encode(root.right, s)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = [int(s) for s in data.split(',')]
        self.start = 0
        return self._decode(data, -sys.maxsize, sys.maxsize)

    def _decode(self, data, min_val, max_val):
        if self.start >= len(data) or data[self.start] < min_val or data[self.start] > max_val:
            return None
        root = TreeNode(data[self.start])
        self.start += 1
        root.left = self._decode(data, min_val, root.val)
        root.right = self._decode(data, root.val, max_val)
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
