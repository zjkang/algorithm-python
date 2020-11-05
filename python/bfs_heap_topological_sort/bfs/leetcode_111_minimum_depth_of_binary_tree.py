"""
author: Zhengjian Kang
date: 10/07/2020

https://leetcode.com/problems/minimum-depth-of-binary-tree/

111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

        3
     / \
    9  20
        /  \
     15   7
return its minimum depth = 2.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque([root])
        depth = 0
        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                head = queue.popleft()
                if not head.left and not head.right:
                    return depth
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
        return 0
