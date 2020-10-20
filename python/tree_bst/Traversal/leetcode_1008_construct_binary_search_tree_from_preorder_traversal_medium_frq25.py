"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

1008. Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 
Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = preorder.pop(0)
            root = TreeNode(val)
            
            idx = idx_map[val]
            
            root.left = helper(in_left, idx - 1)
            root.right = helper(idx + 1, in_right)
            
            return root
        
        return helper(0, len(preorder) - 1)