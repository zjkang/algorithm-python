"""
author: Zhengjian Kang
date: 10/11/2020

https://leetcode.com/problems/remove-duplicate-letters/

316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
 
Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""


from collections import Counter
from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        m = Counter(s)
        visited = defaultdict(int)
        res = ['0']
        for a in s:
            m[a] -= 1
            if visited[a]:
                continue
            while a < res[-1] and m[res[-1]]:
                visited[res[-1]] = 0
                res.pop()
            res.append(a)
            visited[a] = 1
        return ''.join(res[1:])
