"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/binary-tree-maximum-path-sum/

124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

 
Example 1:
Input: root = [1,2,3]
Output: 6

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42

Constraints:

The number of nodes in the tree is in the range [0, 3 * 104].
-1000 <= Node.val <= 1000

"""
# Recursion
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        curr_max_so_far, curr_max_ending_here = self.dfs(root)
        
        return curr_max_so_far
        
    
    def dfs(self, root):
        if not root:
            return float('-inf'), 0
        
        left_max_so_far, left_max_ending_here = self.dfs(root.left)
        right_max_so_far, right_max_ending_here = self.dfs(root.right)
        
        left_max_ending_here = max(0, left_max_ending_here)
        right_max_ending_here = max(0, right_max_ending_here)
        
        curr_max_so_far = max(max(left_max_so_far, right_max_so_far), left_max_ending_here + right_max_ending_here + root.val)
        
        return curr_max_so_far, root.val + max(left_max_ending_here, right_max_ending_here)