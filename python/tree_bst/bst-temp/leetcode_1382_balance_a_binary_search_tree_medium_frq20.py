"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/balance-a-binary-search-tree/

1382. Balance a Binary Search Tree

Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

 

Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            stack, curr = [], root
            inorder = []
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()
                inorder.append(curr.val)
                curr = curr.right
            
            return inorder
        
        
        def build(nodes):
            if not nodes:
                return None
            
            mid = len(nodes) // 2
            root = TreeNode(nodes[mid])
            root.left = build(nodes[:mid])
            root.right = build(nodes[mid + 1:])
            
            return root
        
        return build(inorder(root))
            