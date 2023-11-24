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
        s = s + '+' # enable handle with last operator
        
        stack = [] # nums
        sign = '+' # previous sign
        cur_num = 0

        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                cur_num = cur_num * 10 + ord(s[index]) - ord('0')
                index += 1
                continue

            if sign == '+':
                stack.append(cur_num)
            elif sign == '-':
                stack.append(-cur_num)
            elif sign == '*':
                stack.append(stack.pop() * cur_num)
            elif sign == '/':
                stack.append(int(stack.pop() / cur_num))

            sign = s[index]
            cur_num = 0
            index += 1

        return sum(stack)
