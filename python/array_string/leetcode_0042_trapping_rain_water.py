
"""
author: Zhengjian Kang
date: 03/08/2021

残酷群每日一题: 03/07/2021

https://leetcode.com/problems/trapping-rain-water/

42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
0 <= n <= 3 * 10^4
0 <= height[i] <= 10^5
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res, left_max, right_max = 0, 0, 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if left_max < right_max:
                res += left_max - height[l]
                l += 1
            else:
                res += right_max - height[r]
                r -= 1
        return res
