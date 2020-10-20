"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

889. Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(left_idx, right_idx, N):
            if N == 0:
                return None
            
            root = TreeNode(pre[left_idx])
            
            if N == 1:
                return root
            
            L = 0
            while post[right_idx + L - 1] != pre[left_idx + 1]:
                L += 1
                
            
            root.left = helper(left_idx + 1, right_idx, L)
            root.right = helper(left_idx + L + 1, right_idx + L, N - 1 - L)
            
            return root
        
        return helper(0, 0, len(pre))
             
    
        
            
            
        
            

        
     