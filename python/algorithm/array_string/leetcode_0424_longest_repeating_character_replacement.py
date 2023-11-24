'''
author: Zhengjian Kang
date: 10/06/2021
残酷群每日一题: 10/06/2021

424. Longest Repeating Character Replacement

https://leetcode.com/problems/longest-repeating-character-replacement/

note: sliding window (two pointers), use the template, 内部循环条件窗口大小 - 最高频的数目 > k需要收缩窗口

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 
Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, fix right endpoint
        res = 0
        count = [0] * 26
        slow, fast = 0, 0
        while fast < len(s):
            count[ord(s[fast])-ord('A')] += 1
            while fast - slow + 1 - max(count) > k:
                count[ord(s[slow]) - ord('A')] -= 1
                slow += 1
            res = max(res, fast-slow+1)
            fast += 1
        return res
 
