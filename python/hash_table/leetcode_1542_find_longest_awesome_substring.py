"""
author: Zhengjian Kang
date: 07/03/2021

残酷群每日一题: 07/02/2021

https://leetcode.com/problems/find-longest-awesome-substring/

1542. Find Longest Awesome Substring

note: prefix + hash + state 和1915非常类似的题目
https://github.com/wisdompeak/LeetCode/tree/master/Hash/1915.Number-of-Wonderful-Substrings

Given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it palindrome.
Return the length of the maximum length awesome substring of s.

 
Example 1:
Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.

Example 2:
Input: s = "12345678"
Output: 1

Example 3:
Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.

Example 4:
Input: s = "00"
Output: 2

Constraints:
1 <= s.length <= 10^5
s consists only of digits.
"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        #Prefix+Hash+state
        state = 0 # the odd/even of each char
        state_to_index = {0: -1}
        res = 0
        for idx, c in enumerate(s):
            state = state ^ (1 << (ord(c) - ord('0'))) # current state
            if state in state_to_index:    
                res = max(res, idx - state_to_index[state])
            else:
                state_to_index[state] = idx
            for i in range(10):
                state_j = state ^ (1<<i)
                if state_j in state_to_index:
                    res = max(res, idx - state_to_index[state_j])  
        return res
