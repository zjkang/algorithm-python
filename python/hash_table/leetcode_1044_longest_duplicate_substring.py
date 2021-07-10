"""
author: Zhengjian Kang
date: 07/09/2021

残酷群每日一题: 07/06/2021

https://leetcode.com/problems/longest-duplicate-substring/

1044. Longest Duplicate Substring
note: rolling hash

Given a string s, consider all duplicated substrings:
(contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example 1:
Input: s = "banana"
Output: "ana"

Example 2:
Input: s = "abcd"
Output: ""

Constraints:
2 <= s.length <= 3 * 10^4
s consists of lowercase English letters.
"""

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        left, right = 1, len(s)
        res = ""
        while left + 1 < right:
            mid = (left+right)//2
            if self.found(s, mid):
                left = mid
            else:
                right = mid
        res = self.found(s, right)
        if res: return res
        return self.found(s, left)
    
    def found(self, s, length):
        base = 26; mod = 10**12+7
        hash = 0
        seen = set()
        pow_base_len = 1
        for i in range(length):
            pow_base_len = pow_base_len*base % mod
        
        for i in range(len(s)):
            hash = (hash * base + ord(s[i])-ord('a')) % mod
            if i >= length:
                hash = (hash - pow_base_len*(ord(s[i-length])-ord('a'))% mod + mod) % mod
            if i >= length-1:
                if hash in seen:
                    return s[i-length+1: i+1]
                seen.add(hash)
        return ""
