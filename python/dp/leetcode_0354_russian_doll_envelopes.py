"""
author: Zhengjian Kang
date: 08/23/2021
残酷群每日一题: 08/23/2021

https://leetcode.com/problems/russian-doll-envelopes/
354. Russian Doll Envelopes

note: 2d LIS

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
 

Constraints:
1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 10^4
"""

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # lis
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for a,b in envelopes:
            if not stack or (b>stack[-1]):
                stack.append(b)
            else:
                pos = bisect.bisect_left(stack, b)
                stack[pos] = b
        return len(stack)
 
