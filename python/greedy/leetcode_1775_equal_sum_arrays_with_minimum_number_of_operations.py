
"""
author: Zhengjian Kang
date: 03/04/2021

残酷群每日一题: 03/02/2021

https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

1775. Equal Sum Arrays With Minimum Number of Operations

note: 这道题是双指针的算法，选择贪心的最大下降值

You are given two arrays of integers nums1 and nums2, possibly of different
lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to
any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values
in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible
to make the sum of the two arrays equal.

Example 1:
Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations.
All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].

Example 2:
Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the
sum of nums2 to make them equal.

Example 3:
Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations.
All indices are 0-indexed.
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].

Constraints:
1 <= nums1.length, nums2.length <= 10^5
1 <= nums1[i], nums2[i] <= 6
"""


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 < sum2:
            return self.minOperations(nums2, nums1)

        diff = sum1 - sum2
        nums1.sort()
        nums2.sort()

        # nums1=[1,2,3,4,5,6]
        # nums2=[1,1,2,2,2,2]
        i, j = len(nums1)-1, 0
        count = 0
        while i >= 0 or j < len(nums2):
            old_diff = diff
            gap1, gap2 = -1, -1
            if i >= 0:
                gap1 = nums1[i] - 1
            if j < len(nums2):
                gap2 = 6 - nums2[j]
            if gap1 >= gap2:
                diff -= gap1
                i -= 1
            else:
                diff -= gap2
                j += 1
            if old_diff == diff:
                break
            count += 1
            if diff <= 0:
                return count
        return -1
