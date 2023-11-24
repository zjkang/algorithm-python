'''
76. Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"
 

Constraints:
1 <= s.length, t.length <= 105
s and t consist of English letters.
'''




class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = [0] * 256
        s_freq = [0] * 256
        num_t, num_s = len(t), len(s)
        for c in t:
            t_freq[ord(c)] += 1
        slow, fast = 0, 0
        count = 0
        res = ""
        while fast < num_s:
            index = ord(s[fast])
            if t_freq[index] > 0:
                s_freq[index] += 1
                if s_freq[index] <= t_freq[index]:
                    count += 1
            
            while count == num_t and slow <= fast:
                index = ord(s[slow])
                if not res or fast - slow + 1< len(res):
                    res = s[slow: fast+1]
                if s_freq[index] > 0:
                    s_freq[index] -= 1
                    if s_freq[index] < t_freq[index]:
                        count -= 1
                slow += 1
            fast += 1

        return res
            
        
        
        
