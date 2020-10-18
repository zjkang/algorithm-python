"""
author: Zhengjian Kang
date: 10/17/2020

https://leetcode.com/problems/find-duplicate-subtrees/

652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:

Input: root = [2,1,1]
Output: [[1]]

Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.res = []
        self.dfs(root, {})
        return self.res

    def dfs(self, root, seen):
        if not root:
            return '#'
        left_code = self.dfs(root.left, seen)
        right_code = self.dfs(root.right, seen)
        root_code = str(root.val) + '$' + left_code + right_code
        if root_code in seen:
            if seen[root_code] == 1:
                self.res.append(root)
        else:
            seen[root_code] = 0
        seen[root_code] += 1
        return root_code


# https://medium.com/@lenchen/leetcode-topics-tree-d0ccebb11904
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def dfs(node: TreeNode) -> tuple:
            if not node:
                return None
            hashing = (node.val, dfs(node.left), dfs(node.right))
            counter[hashing] += 1
            if counter[hashing] == 2:
                self.result.append(node)
            return hashing

        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        counter = collections.Counter()
        self.result = []
        dfs(root)
        return self.result
