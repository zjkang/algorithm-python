"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            idx = idx_map[val]
            
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)


            return root
        
        
        return helper(0, len(inorder) - 1)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        in_map = {val: idx for idx, val in enumerate(inorder)}
        return self.helper(in_map, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        
    def helper(self, in_map, istart, iend, postorder, pstart, pend):
        if pstart > pend: return None
        root = TreeNode(postorder[pend])
        imid = in_map[postorder[pend]]
        root.left = self.helper(in_map, istart, imid-1, postorder, pstart, pstart + imid-1-istart)
        root.right = self.helper(in_map, imid+1, iend, postorder, pstart+imid-istart, pend-1)
        return root