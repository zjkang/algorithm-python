"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/binary-search-tree-iterator/

173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Morris
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.node:
            if not self.node.left: break
            child = self.node.left
            while child.right:
                child = child.right
            child.right = self.node
            child = self.node.left
            self.node.left = None
            self.node = child
        value = self.node.val
        self.node = self.node.right
        return value

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.node

# 2
class BSTIterator:

    def __init__(self, root: TreeNode):
        stack, curr = [], root
        self.flattered = []
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
             
            curr = stack.pop()
            self.flattered.append(curr.val)
            curr = curr.right
        
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            return self.flattered.pop(0)
            
                
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.flattered) > 0
