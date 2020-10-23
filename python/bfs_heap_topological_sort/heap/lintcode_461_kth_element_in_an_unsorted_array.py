"""
author: Zhengjian Kang
date: 10/22/2020

https://www.lintcode.com/problem/kth-smallest-numbers-in-unsorted-array/description

461 Kth Smallest Numbers in Unsorted Array

Find the kth smallest number in an unsorted integer array.

Example
Example 1:
Input: [3, 4, 1, 2, 5], k = 3
Output: 3

Example 2:
Input: [1, 1, 1], k = 2
Output: 1
"""


class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        if nums is None:
            return None
        import heapq
        heap_nums = []
        for num in nums:
            if len(heap_nums) < k:
                # max-heap with negating '-' element
                heapq.heappush(heap_nums, -num)
            elif num < -heap_nums[0]:
                heapq.heappop(heap_nums)
                heapq.heappush(heap_nums, -num)
        res = -heapq.heappop(heap_nums)
        return res
