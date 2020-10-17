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
# Non-recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:    
        if not root:
            return True
        
        queue = collections.deque([root.left, root.right])
        
        while queue:
            left = queue.popleft()
            right = queue.pop()
            
            if not left and not right:
                continue
            
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            queue.appendleft(left.left)
            queue.append(right.right)
            
            queue.appendleft(left.right)
            queue.append(right.left)

        return True         

# Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:      
        def helper(node, mirror):
            if not node and not mirror:
                return True
            
            if not node or not mirror:
                return False
            
            
            left = helper(node.left, mirror.right)
            right = helper(node.right, mirror.left)
            
            return node.val == mirror.val and left and right
        
        return helper(root, root)