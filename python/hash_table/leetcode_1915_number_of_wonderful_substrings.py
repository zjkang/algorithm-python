"""
author: Zhengjian Kang
date: 07/02/2021

残酷群每日一题: 07/01/2021

https://leetcode.com/problems/number-of-wonderful-substrings/

1915. Number of Wonderful Substrings

note: prefix + hash + state

https://github.com/wisdompeak/LeetCode/tree/master/Hash/1915.Number-of-Wonderful-Substrings

A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters
('a' through 'j'), return the number of wonderful non-empty substrings in word.
If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"

Example 2:
Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"

Example 3:
Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:
1 <= word.length <= 10^5
word consists of lowercase English letters from 'a' to 'j'.
"""

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        #Prefix+Hash+state
        state = 0 # the odd/even of each char
        count = [0] * (1<<10)
        count[0] = 1
        
        res = 0
        for c in word:
            state = state ^ (1 << (ord(c) - ord('a'))) # current state
            res += count[state]
            for i in range(10):
                state_j = state ^ (1<<i)
                res += count[state_j]    
            
            count[state] += 1
            
        return res
