
"""
author: Zhengjian Kang
date: 03/14/2021

残酷群每日一题: 03/14/2021

https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

1442. Count Triplets That Can Form Two Arrays of Equal XOR

note: pre sum + xor

Given an array of integers arr.
We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
Let's define a and b as follows:
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.
Return the number of triplets (i, j and k) Where a == b.

Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:
Input: arr = [1,1,1,1,1]
Output: 10

Example 3:
Input: arr = [2,3]
Output: 0

Example 4:
Input: arr = [1,3,5,7,9]
Output: 3

Example 5:
Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8

Constraints:
1 <= arr.length <= 300
1 <= arr[i] <= 10^8
"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # use A^A = 0
        pre_xor_sum = defaultdict(list)  # val: [index]
        pre_xor_sum[0].append(-1)
        res = 0
        cur = 0
        for idx, val in enumerate(arr):
            cur = cur ^ val
            if cur not in pre_xor_sum:
                pre_xor_sum[cur].append(idx)
            else:
                for i in pre_xor_sum[cur]:
                    res += idx - (i+1)
                pre_xor_sum[cur].append(idx)
        return res
