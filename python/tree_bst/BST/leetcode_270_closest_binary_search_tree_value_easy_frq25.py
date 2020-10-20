"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/closest-binary-search-tree-value/

270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closet = root.val
        while root:
            closet = min(root.val, closet, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closet