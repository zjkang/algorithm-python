"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/balanced-binary-tree/

110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""
# Recursion
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) != -1
        
    
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        
        return max(left, right) + 1