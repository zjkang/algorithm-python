"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/house-robber-iii/

337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
# Recursion
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))

  def dfs(self, root):
        if not root:
            return 0, 0

        rob_left, not_rob_left = self.dfs(root.left)
        rob_right, not_rob_right = self.dfs(root.right)

        rob_curr = root.val + not_rob_left + not_rob_right
        not_rob_curr = max(rob_left, not_rob_left) + \
            max(rob_right, not_rob_right)

        return rob_curr, not_rob_curr
