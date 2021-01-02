"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/unique-binary-search-trees-ii/

95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

0 <= n <= 8

"""
import functools
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        @functools.lru_cache(None)
        def build(start: int, end: int):
            trees = []
            for root in range(start, end + 1):
                for left_subtree in build(start, root - 1):
                    for right_subtree in build(root + 1, end):
                        node = TreeNode(root)
                        node.left = left_subtree
                        node.right = right_subtree
                        trees.append(node)
            return trees or [None]

        return [] if n == 0 else build(1, n)

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)
                
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)
                
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n) if n else []        