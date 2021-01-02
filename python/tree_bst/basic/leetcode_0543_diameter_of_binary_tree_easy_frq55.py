"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/diameter-of-binary-tree/

543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Recursion


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        diameter, path = self.dfs(root)

        return diameter - 1

    def dfs(self, root):
        if not root:
            return 0, 0

        left_diameter, left_max_path = self.dfs(root.left)
        right_diameter, right_max_path = self.dfs(root.right)

        curr_max_path = max(left_max_path, right_max_path) + 1

        return max(left_diameter, right_diameter, left_max_path + right_max_path + 1), curr_max_path
