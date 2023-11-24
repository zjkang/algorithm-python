"""
author: Zhengjian Kang
date: 03/24/2021

残酷群每日一题: 01/28/2021

https://leetcode.com/problems/find-all-duplicates-in-an-array/

442. Find All Duplicates in an Array

note: index sort

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = []
        start = 0
        while start < len(nums):
            while nums[start] != (start + 1):
                j = nums[start] - 1
                if nums[start] == nums[j]:
                    break
                nums[start], nums[j] = nums[j], nums[start]
            start += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
        return res
