"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        return self.helper(nums, 0, len(nums) - 1)
     
    def helper(self, nums, start, end):
        if start > end:
            return None

        if start == end:
            return TreeNode(nums[0])

        mid = (start + end) // 2

        root = TreeNode(nums[mid])
        root.left = self.helper(nums, start, mid - 1)
        root.right = self.helper(nums, mid + 1, end)            

        return root