
"""
author: Zhengjian Kang
date: 03/24/2021

残酷群每日一题: 01/29/2021

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

448. Find All Numbers Disappeared in an Array

note: index sort

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                j = nums[i]-1
                nums[i], nums[j] = nums[j], nums[i]
        return [i+1 for i in range(n) if nums[i] != i+1]
