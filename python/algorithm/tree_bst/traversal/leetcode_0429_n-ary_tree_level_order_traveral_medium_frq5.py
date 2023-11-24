"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/n-ary-tree-level-order-traversal/

429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Non-recursion
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []
        
        while queue:
            size = len(queue)
            
            formed = []
            for _ in range(size):
                node = queue.popleft()
                
                formed.append(node.val)
                queue += node.children
            
            result.append(formed)
       
        return result

# Recursion
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        result = []
        def helper(root, level):
            if level == len(result):
                result.append([])

            result[level].append(root.val)
            for child in root.children:
                helper(child, level + 1)
        
        helper(root, 0)
        
        return result
    