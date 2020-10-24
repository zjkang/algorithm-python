"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        
        stack, curr = [], root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            k -= 1
            if not k:
                return curr.val
    
            curr = curr.right
            
# Morris inorder tranversal
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        while root:
            if child := root.left:
                while child.right and child.right is not root:
                    child = child.right
                if child.right is root:
                    child.right = None
                    k -= 1
                    if k == 0: break
                    root = root.right
                else:
                    child.right = root
                    root = root.left
            else:
                k -= 1
                if k == 0: break
                root = root.right
        return root.val