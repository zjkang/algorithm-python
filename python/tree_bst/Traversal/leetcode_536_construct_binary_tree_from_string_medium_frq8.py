"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/construct-binary-tree-from-string/

536. Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

 

Example 1:
Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Example 2:
Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]

Example 3:
Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
 

Constraints:

0 <= s.length <= 3 * 104
s consists of digits, '(', ')', and '-' only.
"""            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        
        stack, num, s = [TreeNode(0)], '', s + '('
        
        for i, c in enumerate(s):
            if c == ')':
                stack.pop()
            else:
                if c != '(':
                    num += c
                    if not s[i + 1].isdigit():
                        node = TreeNode(int(num))
                        
                        if stack[-1].left:
                            stack[-1].right = node
                        else:
                            stack[-1].left = node
                            
                        stack.append(node) 
                        num = ''
        
        return stack[0].left