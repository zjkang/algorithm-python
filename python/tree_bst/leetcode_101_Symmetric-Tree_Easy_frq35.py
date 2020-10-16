"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/symmetric-tree/

101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Follow up: Solve it both recursively and iteratively.
"""
# Recursion
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))
        
    
    def dfs(self, root):
        if not root:
            return 0, 0
        
        rob_left, not_rob_left = self.dfs(root.left)
        rob_right, not_rob_right = self.dfs(root.right)
        
        rob_curr = root.val + not_rob_left + not_rob_right
        not_rob_curr = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
        
        return rob_curr, not_rob_curr