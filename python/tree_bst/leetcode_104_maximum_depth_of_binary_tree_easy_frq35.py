"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/maximum-depth-of-binary-tree/

104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""            
# top-down Recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.max_depth = 0
        self.dfs(root, 1)
        
        return self.max_depth
    
    def dfs(self, root, depth):
        if not root:
            return
        
        if not root.left and not root.right:
            self.max_depth = max(self.max_depth, depth)
            
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
            

# Bottom-up Recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return max(left, right) + 1   