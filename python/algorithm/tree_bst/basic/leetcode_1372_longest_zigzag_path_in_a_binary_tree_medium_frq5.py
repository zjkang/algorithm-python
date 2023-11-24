"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

1372. Longest ZigZag Path in a Binary Tree

Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right then move to the right child of the current node otherwise move to the left child.
Change the direction from right to left or right to left.
Repeat the second and third step until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0
 

Constraints:

Each tree has at most 50000 nodes..
Each node's value is between [1, 100].

"""
# Top down recursion
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_len = 0
        self.dfs(root, True, 0)
        
        return self.max_len
    
    
    def dfs(self, root, is_left, depth):
        self.max_len = max(self.max_len, depth)
        
        if is_left:
            if root.left:
                self.dfs(root.left, True, 1)
            
            if root.right:
                self.dfs(root.right, False, depth + 1)
        
        else:
            if root.left:
                self.dfs(root.left, True, depth + 1)
            
            if root.right:
                self.dfs(root.right, False, 1)

                
# bottom-up Recursion
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        return self.dfs(root)[2]
    
    def dfs(self, root):
        if not root:
            return -1, -1, -1
        
        left_left, left_right, left_max,  = self.dfs(root.left)
        right_left, right_right, right_max = self.dfs(root.right)
        
        curr_max = max(left_max, right_max, left_right + 1, right_left + 1)
        curr_left = left_right + 1
        curr_right = right_left + 1

        return curr_left, curr_right, curr_max