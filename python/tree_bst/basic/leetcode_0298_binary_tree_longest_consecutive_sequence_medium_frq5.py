"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:
Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""            
# top-down Recursion
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_len = 0
        self.dfs(root, None, 0)
        
        return self.max_len
        
    def dfs(self, root, parent, length):
        if not root:
            return
        
        if parent and root.val == parent.val + 1:
            length += 1
        else:
            length = 1
        
        self.max_len = max(self.max_len, length)
        
        self.dfs(root.left, root, length)
        self.dfs(root.right, root, length)

# Bottom-up Recursion
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        curr_max_so_far, curr_max_ending_here = self.dfs(root)
        
        return curr_max_so_far
    
    def dfs(self, root):
        if not root:
            return 0, 0
        
        left_max_so_far, left_max_ending_here = self.dfs(root.left)
        right_max_so_far, right_max_ending_here = self.dfs(root.right)
        
        curr_max_ending_here = 1
        if root.left and root.val + 1 == root.left.val:
            curr_max_ending_here = left_max_ending_here + 1
        
        if root.right and root.val + 1 == root.right.val:
            curr_max_ending_here = max(curr_max_ending_here, right_max_ending_here + 1) 
    
        
        curr_max_so_far = max(max(left_max_so_far, right_max_so_far), curr_max_ending_here)
        
        return curr_max_so_far, curr_max_ending_here     