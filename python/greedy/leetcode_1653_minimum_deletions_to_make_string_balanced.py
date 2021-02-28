
"""
author: Zhengjian Kang
date: 02/28/2021

残酷群每日一题: 02/27/2021

note: 寻找切割点，切割点前都是a,切割点后都是b

https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

1653. Minimum Deletions to Make String Balanced

You are given a string s consisting only of characters 'a' and 'b'​​​​.
You can delete any number of characters in s to make s balanced. s is balanced
if there is no pair of indices (i,j) such that i < j and s[i] = 'b'
and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

Example 1:
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"),
or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

Constraints:
1 <= s.length <= 10^5
s[i] is 'a' or 'b'​​.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        # two pass
        n = len(s)
        # pre[i]: # of 'b' in [0,i]
        pre = [0] * n
        pre[0] = 1 if s[0] == 'b' else 0
        for i in range(1, n):
            pre[i] = pre[i-1] + (1 if s[i] == 'b' else 0)

        # post[i]: # of 'a' in [i,n-1]
        post = [0] * n
        post[-1] = 1 if s[-1] == 'a' else 0
        for i in range(n-2, -1, -1):
            post[i] = post[i+1] + (1 if s[i] == 'a' else 0)

        res = min(pre[-1], post[0])
        for i in range(n-1):
            res = min(res, pre[i] + post[i+1])
        return res
