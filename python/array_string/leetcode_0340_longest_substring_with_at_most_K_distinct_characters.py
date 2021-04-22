'''
340. Longest Substring with At Most K Distinct Characters

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string s and an integer k, return the length of the longest substring of s 
that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:
1 <= s.length <= 5 * 10^4
0 <= k <= 50
'''

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        slow, fast = 0, 0
        freq_map = defaultdict(int)
        res = 0
        while fast < n:
            freq_map[s[fast]] += 1 
            while len(freq_map) > k:
                freq_map[s[slow]] -= 1
                if freq_map[s[slow]] == 0:
                    freq_map.pop(s[slow])
                slow += 1
            res = max(res, fast-slow+1)
            fast += 1
        return res
