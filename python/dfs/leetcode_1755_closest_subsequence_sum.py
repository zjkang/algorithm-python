
"""
author: Zhengjian Kang
date: 02/11/2021

残酷群每日一题: 02/11/2021, 10/21/2021

https://leetcode.com/problems/closest-subsequence-sum/
1755. Closest Subsequence Sum

note: 这是一道非常好的题目。和我当年面试狗家的面试题，给定一个数组，求所有的subset的和很类似
[1,2,3] -> {1,2,3,4,5,6}

https://www.youtube.com/watch?v=h0CpI4N813Q&t=485s

可能的思路
1.参考求subset的dfs穷解法
2.如果sum的值在一个可以确定的范围，dp01背包问题
  类似于leetcode 416 partition equal subset sum

这道题由于数组长度40，可以拆解成20，20，这样每一个subset sum的复杂度2^20，
可以保证不超时

You are given an integer array nums and an integer goal.
You want to choose a subsequence of nums such that the sum of its elements
is the closest possible to goal. That is, if the sum of the subsequence's
elements is sum, then you want to minimize the absolute difference
abs(sum - goal).
Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some
elements (possibly all or none) of the original array.

Example 1:
Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.

Example 2:
Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.

Example 3:
Input: nums = [1,2,3], goal = -7
Output: 7

Constraints:

1 <= nums.length <= 40
-10^7 <= nums[i] <= 10^7
-10^9 <= goal <= 10^9
"""


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        p1 = sorted(self.subset_sum(nums[:n//2]))
        p2 = self.subset_sum(nums[n//2:])
        ans = float('inf')
        for i in p2:
            k = bisect_left(p1, goal - i)
            if k < len(p1):
                ans = min(ans, abs(i + p1[k] - goal))
            if k > 0:
                ans = min(ans, abs(i + p1[k-1] - goal))
        return ans

    def subset_sum(self, nums):
        # time complexity: 2^n
        ans = {0}
        for n in nums:
            ans |= {x + n for x in ans}
        return ans
