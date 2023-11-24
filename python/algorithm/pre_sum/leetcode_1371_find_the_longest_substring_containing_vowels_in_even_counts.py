'''
author: Zhengjian Kang
date: 10/08/2021

残酷群每日一题: 10/08/2021

1371. Find the Longest Substring Containing Vowels in Even Counts

https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

note: prefix word freq count + hash + state compression

Given the string s, return the size of the longest substring containing each vowel an even number of times.
That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

Example 1:
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

Example 2:
Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.

Example 3:
Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

Constraints:
1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
'''

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # prefix word freq count + hash + state compression
        # subarray, substring to consider prefix
        vowel_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state_to_idx = {0: -1} # uoiea
        state = 0
        res = 0
        for idx, c in enumerate(s):
            if c in vowel_map:
                state = state ^ (1 << vowel_map[c])
            if state in state_to_idx:
                res = max(res, idx - state_to_idx[state])
            else:
                state_to_idx[state] = idx
        return res
