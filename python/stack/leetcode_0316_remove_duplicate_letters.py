"""
author: Zhengjian Kang
date: 10/16/2021

残酷群每日一题: 10/12/2021
https://leetcode.com/problems/remove-duplicate-letters/

316. Remove Duplicate Letters
note: 单调栈+greedy 和1081一样的题目 每次挑选最小的sequence

Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""

from collections import Counter
from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # maintain monotonous increasing stack, but can be 'adebc'
        # if character exits in the stack, continue (connot push to resulst)
        # otherwise if character does not appear or comply with increasing stack,
        # push to the stack
        count = Counter(s)
        visited = defaultdict(bool)
        stack = []
        for ch in s:
            count[ch] -= 1
            if visited[ch]: continue
            
            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                visited[stack[-1]] = False
                stack.pop()
            
            stack.append(ch)
            visited[ch] = True
            
        return ''.join(stack[:])
