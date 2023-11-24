"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/validate-binary-search-tree/

98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:    
        def helper(root, lo = float('-inf'), hi = float('inf')):
            if not root:
                return True
            
            if root.val <= lo or root.val >= hi:
                return False
            
            return helper(root.left, lo, root.val) and helper(root.right, root.val, hi)
    
        
        return helper(root)

# Non-recursion
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:    
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, lo, hi = stack.pop()
            
            if not node:
                continue
            
            if node.val <= lo or node.val >= hi:
                return False
                
            stack.append((node.right, node.val, hi))
            stack.append((node.left, lo, node.val))

        return True    