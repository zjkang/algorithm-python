"""
author: Zhengjian Kang
date: 11/29/2020

https://leetcode.com/problems/subarray-sums-divisible-by-k/

974. Subarray Sums Divisible by K

Given an array A of integers, return the number of (contiguous, non-empty)
subarrays that have a sum divisible by K.

Example 1:
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        from collections import defaultdict
        num_map = defaultdict(int)
        num_map[0] = 1
        presum = 0
        for i, num in enumerate(A):
            presum += num
            mod = presum % K

            ans += num_map[mod]
            num_map[mod] += 1

        return ans
