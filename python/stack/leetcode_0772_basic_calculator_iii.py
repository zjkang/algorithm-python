'''
772. Basic Calculator III

https://leetcode.com/problems/basic-calculator-iii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators,
and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
such as eval().

Example 1:
Input: s = "1+1"
Output: 2

Example 2:
Input: s = "6-4/2"
Output: 4

Example 3:
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Example 4:
Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12

Example 5:
Input: s = "0"
Output: 0

Constraints:
1 <= s <= 10^4
s consists of digits, '+', '-', '*', '/', '(', and ')'.
s is a valid expression.
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
