"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/flip-equivalent-binary-trees/

951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivelent or false otherwise.

 

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false
Example 4:

Input: root1 = [0,null,1], root2 = []
Output: false
Example 5:

Input: root1 = [0,null,1], root2 = [0,1]
Output: true
 

Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
"""
# Non-recursion
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        queue1 = collections.deque([root1])
        queue2 = collections.deque([root2])
        
        while queue1 and queue2:
            root1, root2 = queue1.popleft(), queue2.popleft()
            
            if not root1 and not root2:
                continue
            
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            
            if (root1.left and root1.left.val) == (root2.left and root2.left.val):
                queue1 += [root1.left, root1.right]
            else:
                queue1 += [root1.right, root1.left]
            
            queue2 += [root2.left, root2.right]
         
        return True

# Recursion
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
    
            
            left1 = helper(root1.left, root2.left)
            left2 = helper(root1.left, root2.right)
            
            right1 = helper(root1.right, root2.left)
            right2 = helper(root1.right, root2.right)
            
            return (left1 and right2) or (left2 and right1)
       
        return helper(root1, root2)