'''
224. Basic Calculator

https://leetcode.com/problems/basic-calculator/

Given a string s representing an expression, implement a basic calculator to evaluate it.

note: +,-,(,) calculation

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'''


class Solution:
    def calculate(self, s: str) -> int:
        # https://github.com/wisdompeak/LeetCode/tree/master/Stack/224.Basic-Calculator
        res = 0
        sign = 1
        i = 0
        num_stack = []
        sign_stack = []
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] == '+' or s[i] == '-':
                sign = 1 if s[i] == '+' else -1
            elif s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1 # to step back 1 position
                res += num*sign
            elif s[i] == '(':
                # save current computation
                num_stack.append(res)
                sign_stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res = num_stack[-1]+sign_stack[-1]*res
                sign_stack.pop()
                num_stack.pop()
            i += 1
        return res
