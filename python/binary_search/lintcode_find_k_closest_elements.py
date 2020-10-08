"""
author: Zhengjian Kang
date: 10/07/2020

https://www.lintcode.com/problem/find-k-closest-elements/description

460. Find K Closest Elements

Description
Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

The value k is a non-negative integer and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
​​ 
Absolute value of elements in the array will not exceed 10^4
​​ 
Have you met this question in a real interview?  
Example
Example 1:

Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
Challenge
O(logn + k) time
"""


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        if len(A) == 0 or k == 0:
            return []

        pos = self.findClosestNumber(A, target)

        res = []
        res.append(A[pos])
        i = pos - 1
        j = pos + 1

        while i >= 0 and j < len(A) and len(res) < k:
            if abs(A[i] - target) <= abs(A[j] - target):
                res.append(A[i])
                i -= 1
            else:
                res.append(A[j])
                j += 1

        while i >= 0 and len(res) < k:
            res.append(A[i])
            i -= 1

        while j < len(A) and len(res) < k:
            res.append(A[j])
            j += 1

        return res

    def findClosestNumber(self, A, target):
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if abs(target - A[start]) <= abs(target - A[end]):
            return start
        return end
