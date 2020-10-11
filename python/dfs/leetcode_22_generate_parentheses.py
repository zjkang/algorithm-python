"""
author: Zhengjian Kang
date: 10/10/2020

https://leetcode.com/problems/generate-parentheses/

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        if n <= 0:
            return self.res
        valid_paren = []
        self.dfs(n, n, valid_paren)
        return self.res

    def dfs(self, left, right, valid_paren):
        if left == 0 and right == 0:
            self.res.append(''.join(valid_paren))
            return
        if left > 0:
            valid_paren.append('(')
            self.dfs(left - 1, right, valid_paren)
            valid_paren.pop()
        if right > left:
            valid_paren.append(')')
            self.dfs(left, right - 1, valid_paren)
            valid_paren.pop()
