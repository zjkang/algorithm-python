"""
author: Wei Li
date: 10/15/2020

残酷群每日一题: 02/06/2021

https://leetcode.com/problems/subtree-of-another-tree/

572. Subtree of Another Tree

note: 这道题也可以使用KMP

Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a
subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
# Non-recursion


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def pre_order(root, ans):
            if not root:
                ans.append('null')
                return

            ans.append('#' + str(root.val) + '#')

            pre_order(root.left, ans)
            pre_order(root.right, ans)

        s_tree, t_tree = [], []
        pre_order(s, s_tree)
        pre_order(t, t_tree)

        return "".join(t_tree) in "".join(s_tree)


# Recursion
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_matched(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False

            return x.val == y.val and is_matched(x.left, y.left) and is_matched(x.right, y.right)

        if is_matched(s, t):
            return True

        if not s:
            return False

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
