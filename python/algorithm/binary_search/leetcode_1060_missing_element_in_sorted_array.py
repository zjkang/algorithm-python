"""
author: Zhengjian Kang
date: 10/27/2020

https://leetcode.com/problems/missing-element-in-sorted-array/

1060. Missing Element in Sorted Array

Given a sorted array A of unique numbers, find the K-th missing number
starting from the leftmost number of the array.

Example 1:
Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.

Example 2:
Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:
Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums) - 1
        # search index refers to the idx of the element that has the largest smaller val than the wanted missing val
        while start + 1 < end:
            mid = (start + end) // 2
            missing = nums[mid] - nums[0] - mid
            if missing >= k:
                end = mid
            else:
                start = mid
        # nums[pos] + k - (no. already missing on the left)
        if nums[end] - nums[0] - end < k:
            return nums[end] + (k - (nums[end] - nums[0] - end))
        return nums[start] + (k - (nums[start] - nums[0] - start))
