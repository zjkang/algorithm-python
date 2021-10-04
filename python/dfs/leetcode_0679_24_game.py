"""
author: Zhengjian Kang
date: 10/04/2021

残酷群每日一题: 10/03/2021
https://leetcode.com/problems/24-game/

679. 24 Game
note: 对于左右半边枚举结果，做dfs, 与LC 241 Different Ways to Add Parentheses与LC 2019 The Score of Students Solving Math Expression类似的套路

You are given an integer array cards of length 4.
You have four cards, each containing a number in the range [1, 9].
You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/']
and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.

Example 1:
Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: cards = [1,2,1,2]
Output: false
 

Constraints:
cards.length == 4
1 <= cards[i] <= 9
"""

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        from itertools import permutations
        perm = permutations(cards)
        
        def dfs(nums, start, end):
            if start == end:
                return set([nums[start]])
            
            rets = set()
            for i in range(start, end):
                left = dfs(nums, start, i)
                right = dfs(nums, i+1, end)
                for l in left:
                    for r in right:
                        rets.add(l+r)
                        rets.add(l-r)
                        rets.add(l*r)
                        if r != 0:
                            rets.add(l/r)
            return rets
        
        for nums in list(perm):
            rets = dfs(nums, 0, 3)
            for x in rets:
                if abs(x-24.0) <= 10**-6:
                    return True
        return False
 
