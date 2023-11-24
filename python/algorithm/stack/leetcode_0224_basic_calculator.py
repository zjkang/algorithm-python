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
        if not s: return 0
        S = s + '+' # add extra '+' to end as denoting sign
        
        def helper(index):
            cur_num = 0
            sign = "+" # previous sign
            stack = []

            while index < len(S):
                c = S[index]
                if c == ' ':
                    index += 1
                    continue
                if c.isdigit():
                    cur_num = cur_num * 10 + int(c)
                    index += 1
                    continue
                if c == '(':
                    cur_num, index = helper(index + 1)
                else: # on operators
                    if sign == '+':
                        stack.append(cur_num)
                    elif sign == '-':
                        stack.append(-cur_num)
                    elif sign == ')':
                        break
                    cur_num = 0
                    sign = c
                    index += 1
           
            return sum(stack), index
        
        return helper(0)[0]
