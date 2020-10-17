"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/path-sum-iii/

437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        hash_map = collections.defaultdict(int)
        hash_map[0] = 1
        return self.dfs(root, 0, sum, hash_map)

    def dfs(self, root, curr_sum, target, hash_map):
        count = 0
        if not root:
            return 0

        curr_sum += root.val
        count += hash_map[curr_sum - target]

        hash_map[curr_sum] += 1

        count += self.dfs(root.left, curr_sum, target, hash_map)
        count += self.dfs(root.right, curr_sum, target, hash_map)

        hash_map[curr_sum] -= 1

        return count
