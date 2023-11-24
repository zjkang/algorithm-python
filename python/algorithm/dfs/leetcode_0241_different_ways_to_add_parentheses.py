"""
author: Zhengjian Kang
date: 10/04/2021

残酷群每日一题: 10/01/2021
https://leetcode.com/problems/different-ways-to-add-parentheses/

241. Different Ways to Add Parentheses
note: 对于左右半边枚举结果，做dfs

Given a string expression of numbers and operators,
return all possible results from computing all the different possible ways to group numbers and operators.
You may return the answer in any order.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
"""

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # dfs or dfs + momo
        memo = {}
        def comp(s):
            if s in memo:
                return memo[s]
            operators = ['+', '-', '*']
            res = []
            for i in range(len(s)):
                if s[i] in operators:
                    op = s[i]
                    left = s[:i]
                    right = s[i+1:]
                    left_res = comp(left)
                    right_res = comp(right)
                    for x in left_res:
                        for y in right_res:
                            if op == '+':
                                res.append(x+y)
                            elif op == '-':
                                res.append(x-y)
                            elif op == '*':
                                res.append(x*y)
            if len(res) == 0:
                res.append(int(s))
            memo[s] = res
            return res

        r = comp(expression)
        return r
