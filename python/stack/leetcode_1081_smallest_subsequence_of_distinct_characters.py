"""
author: Zhengjian Kang
date: 10/14/2021

残酷群每日一题: 10/13/2021
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

1081. Smallest Subsequence of Distinct Characters

note: 单调栈+greedy 和316一样的题目 每次挑选最小的sequence

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def smallestSubsequence(self, s: str) -> str:
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
