"""
author: Zhengjian Kang
date: 01/27/2021

残酷群每日一题: 03/20/2021; 01/23/2021

https://leetcode.com/problems/decode-xored-permutation/

1734. Decode XORed Permutation

note:利用奇偶的性质做xor

There is an integer array perm that is a permutation of the first n positive
integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that
encoded[i] = perm[i] XOR perm[i + 1].
For example, if perm = [1,3,2], then encoded = [2,1].
Given the encoded array, return the original array perm. It is guaranteed
that the answer exists and is unique.

Example 1:
Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]

Example 2:
Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]

Constraints:
3 <= n < 10^5
n is odd.
encoded.length == n - 1
"""


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        x, n = 0, len(encoded)+1
        for i in range(1, n+1):
            x = x ^ i
        # perm[0] = x XOR encoded[1] XOR encoded[3] XOR encoded[5]
        for i in range(1, len(encoded), 2):
            x = x ^ encoded[i]
        res = [0] * n
        res[0] = x
        for i in range(len(encoded)):
            res[i+1] = res[i] ^ encoded[i]
        return res
