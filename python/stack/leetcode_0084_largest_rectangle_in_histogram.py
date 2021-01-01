"""
author: Zhengjian Kang
date: 12/31/2020

https://leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where
the width of each bar is 1, find the area of largest rectangle in the
histogram.

Above is a histogram where width of each bar is 1, given
height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""


class Solution:
    # brute force: expand from the center, require time complexity O(n^2)
    # use increasing stack to determine left and right boundary
    # right boundary: the index smaller than stack top element
    # left boundary: the index next to stack top
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [0]
        i = 1
        heights.insert(0, -1)
        # print(heights)
        while i < len(heights):
            while stack and heights[stack[-1]] > heights[i]:
                left_idx = stack.pop()
                res = max(res, (i - stack[-1]-1) * heights[left_idx])
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            # print(stack)
            i += 1
        # print('test')
        while len(stack) > 1:
            left_idx = stack.pop()
            res = max(res, (len(heights) - stack[-1] - 1) * heights[left_idx])
        return res
