"""
author: Zhengjian Kang
date: 08/17/2021
残酷群每日一题: 08/16/2021

https://leetcode.com/problems/valid-parenthesis-string/
678. Valid Parenthesis String

note: greedy + max/min # of unmatched left parenthesis 

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true
 
Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""

class Solution:
    # https://github.com/wisdompeak/LeetCode/tree/master/Greedy/678.Valid-Parenthesis-String
    def checkValidString(self, s: str) -> bool:
        count_max, count_min = 0, 0
        for ch in s:
            if ch == '(':
                count_max += 1
                count_min += 1
            elif ch == ')':
                count_max -= 1
                count_min -= 1
            else:
                count_max += 1
                count_min -= 1
            # too many )
            if count_max < 0:
                return False
            # reset
            if count_min < 0:
                count_min = 0
        return count_min == 0
