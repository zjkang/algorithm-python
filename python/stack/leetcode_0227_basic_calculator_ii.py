'''
227. Basic Calculator II

https://leetcode.com/problems/basic-calculator-ii/

note: +,-,*,/

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
 
Constraints:
1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign_stack = []
        sign = 1
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
                num = num * sign
                if sign_stack:
                    new_sign = 1 if stack[-1]*num > 0 else -1
                    if sign_stack[-1]=='*':
                        num = stack[-1]*num
                    else:
                        # note: -3/2==-2
                        num = new_sign * (abs(stack[-1])//abs(num))
                    stack.pop()
                    sign_stack.pop()
                stack.append(num)
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '*' or s[i] == '/':
                sign = 1
                sign_stack.append(s[i])
            i += 1
        
        return sum(stack)
