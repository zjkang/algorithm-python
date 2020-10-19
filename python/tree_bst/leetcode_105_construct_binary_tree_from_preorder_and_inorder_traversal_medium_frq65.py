"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            root = TreeNode(preorder.pop(0))
            idx = idx_map[root.val]
            
            root.left = helper(in_left, idx - 1)
            root.right = helper(idx + 1, in_right)
            
            return root
       
        return helper(0, len(inorder) - 1)