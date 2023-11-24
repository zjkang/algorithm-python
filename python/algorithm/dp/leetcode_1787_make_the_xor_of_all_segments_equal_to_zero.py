
"""
author: Zhengjian Kang
date: 03/13/2021

残酷群每日一题: 03/11/2021

https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

1787. Make the XOR of All Segments Equal to Zero

note: 完全没思路的题，照着群主看了一下
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1787.Make-the-XOR-of-All-Segments-Equal-to-Zero

You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment
[left, right] where left <= right is the XOR of all the elements with indices
between left and right, inclusive: nums[left] XOR nums[left+1] XOR ...
XOR nums[right].

Return the minimum number of elements to change in the array such that the
XOR of all segments of size k​​​​​​ is equal to zero.

Example 1:
Input: nums = [1,2,0,3,0], k = 1
Output: 3
Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].

Example 2:
Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
Output: 3
Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].

Example 3:
Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
Output: 3
Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].

Constraints:
1 <= k <= nums.length <= 2000
​​​​​​0 <= nums[i] < 2^10
"""


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # count frequencies on each segment column
        counters = [Counter() for _ in range(k)]
        for i, v in enumerate(nums):
            counters[i % k][v] += 1

        # use dp to compute minimum changes
        num_cnts = [sum(cnt.values()) for cnt in counters]
        dp = [[float('inf')] * 1024 for _ in range(k)]
        for x in range(1024):
            dp[-1][x] = num_cnts[-1] - counters[-1][x]  # base case

        for i in range(k-2, -1, -1):
            # assuming counters[i][v] == 0, change all column i to a new value
            change_all_cost = num_cnts[i] + min(dp[i+1])
            for x in range(1024):
                best_res = change_all_cost
                for v in counters[i].keys():
                    tmp = num_cnts[i] - counters[i][v] + dp[i+1][x ^ v]
                    best_res = min(best_res, tmp)
                dp[i][x] = best_res
        return dp[0][0]
