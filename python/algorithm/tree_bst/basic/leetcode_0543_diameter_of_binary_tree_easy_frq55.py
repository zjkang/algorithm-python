"""
author: Zhengjian Kang
date: 11/01/2021

残酷群每日一题: 11/01/2021

https://leetcode.com/problems/diameter-of-binary-tree/

543. Diameter of Binary Tree

note: recursion

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        g_length = [0]
        def dfs(root):
            if not root: return 0
            left_len = dfs(root.left)
            right_len = dfs(root.right)
            g_length[0] = max(g_length[0], 1 + left_len + right_len)
            return 1 + max(left_len, right_len)
        
        dfs(root)
        return 0 if g_length[0] == 0 else g_length[0] - 1
