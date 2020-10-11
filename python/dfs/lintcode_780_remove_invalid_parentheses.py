"""
author: Zhengjian Kang
date: 10/11/2020

https://www.lintcode.com/problem/remove-invalid-parentheses/description

780. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Example
Example 1:

Input:
"()())()"
Ouput:
["(())()","()()()"]
Example 2:

Input:
"(a)())()"
Output:
 ["(a)()()", "(a())()"]
Example 3:

Input:
")(" 
Output:
 [""]
"""


class Solution:
    def removeInvalidParentheses(self, s):
        res = []
        left, right = self._LeftRightCount(s)
        self._dfs(s, left, right, 0, res)
        return res

    def _dfs(self, s, left, right, start, res):
        if left == 0 and right == 0:
            if self._isvalid(s):
                res.append(s)
            return
        for i in range(start, len(s)):
            if i > start and s[i] == s[i-1]:
                continue
            if s[i] == '(' and left >= 1:
                self._dfs(s[:i]+s[i+1:], left-1, right, i, res)
            if s[i] == ')' and right >= 1:
                self._dfs(s[:i]+s[i+1:], left, right-1, i, res)

    def _isvalid(self, s):
        left, right = self._LeftRightCount(s)
        return left == 0 and right == 0

    # minimum # of left/right breaking balanced parenthesis to confirm valid result
    # )(: left=right=1
    def _LeftRightCount(self, s):
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right
