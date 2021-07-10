"""
author: Zhengjian Kang
date: 07/09/2021

残酷群每日一题: 07/09/2021

https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

1698. Number of Distinct Substrings in a String
note: rolling hash O(n^2)

Given a string s, return the number of distinct substrings of s.

A substring of a string is obtained by deleting any number of characters
(possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

Example 1:
Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is
["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]

Example 2:
Input: s = "abcdefg"
Output: 28

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
Follow up: Can you solve this problem in O(n) time complexity?
"""

class Solution:
    def countDistinct(self, s: str) -> int:
        N = len(s)
        base = 26
        count = 0
        for l in range(1, N+1):
            hash = 0
            power = pow(base, l-1)
            seen = set()
            for i in range(N):
                if i-l >= 0:
                    hash -= (ord(s[i-l]) - ord('a')) * power
                hash = hash * base + (ord(s[i]) - ord('a'))
                if i >= l-1 :
                    seen.add(hash)
            count += len(seen)
        return count
 
