
"""
author: Zhengjian Kang
date: 03/21/2021

残酷群每日一题: 01/30/2021

https://leetcode.com/problems/set-mismatch/

645. Set Mismatch

You have a set of integers s, which originally contains all the numbers from 1
to n. Unfortunately, due to some error, one of the numbers in s got duplicated
to another number in the set, which results in repetition of one number and
loss of another number.

You are given an integer array nums representing the data status of this set
after the error.

Find the number that occurs twice and the number that is missing and return
them in the form of an array.


Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                s = nums[i]
                if nums[i] == nums[s-1]:
                    break
                nums[i], nums[s-1] = nums[s-1], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
