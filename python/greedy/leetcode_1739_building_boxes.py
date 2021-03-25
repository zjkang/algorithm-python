
"""
author: Zhengjian Kang
date: 03/24/2021

残酷群每日一题: 01/26/2021

https://leetcode.com/problems/building-boxes/

1739. Building Boxes

note: greedy + binary search

You have a cubic storeroom where the width, length, and height of the room
are all equal to n units. You are asked to place n boxes in this room where
each box is a cube of unit side length. There are however some rules to
placing the boxes:

You can place the boxes anywhere on the floor.
If box x is placed on top of the box y, then each side of the four vertical
sides of the box y must either be adjacent to another box or to a wall.
Given an integer n, return the minimum possible number of boxes touching the
floor.

Example 1:
Input: n = 3
Output: 3
Explanation: The figure above is for the placement of the three boxes.
These boxes are placed in the corner of the room, where the corner is on the
left side.

Example 2:
Input: n = 4
Output: 3
Explanation: The figure above is for the placement of the four boxes.
These boxes are placed in the corner of the room, where the corner is on the
left side.

Example 3:
Input: n = 10
Output: 6
Explanation: The figure above is for the placement of the ten boxes.
These boxes are placed in the corner of the room, where the corner is on
the back side.

Constraints:
1 <= n <= 10^9
"""


class Solution:
    def minimumBoxes(self, n: int) -> int:
        def cal(area):
            d = int(math.sqrt(2*area))
            if (1+d)*d//2 > area:
                d -= 1
            diff = area - (1+d)*d//2
            nums = [0] * d
            for i in range(d):
                nums[i] = d-i
            for i in range(diff):
                nums[i] += 1

            post_sum = 0
            total = 0
            for i in range(d-1, -1, -1):
                post_sum += nums[i]
                total += post_sum
            return total

        left = 0
        right = 10**9
        while left < right:
            mid = (left + right) // 2
            if cal(mid) >= n:
                right = mid
            else:
                left = mid+1
        return left
