"""
author: Zhengjian Kang
date: 03/24/2021

残酷群每日一题: 01/27/2021

https://leetcode.com/problems/find-the-duplicate-number/

287. Find the Duplicate Number

note: index sort

Given an array of integers nums containing n + 1 integers where each integer
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1

Constraints:
2 <= n <= 3 * 10^4
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer
which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i+1:
                j = nums[i] - 1
                if nums[i] == nums[j]:
                    return nums[i]
                nums[i], nums[j] = nums[j], nums[i]
        return -1
