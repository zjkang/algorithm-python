"""
author: Zhengjian Kang
date: 10/22/2020

https://www.lintcode.com/problem/heapify/description

130. Heapify

Given an integer array, heapify it into a min-heap array.
For a heap array A, A[0] is the root of heap, and for each A[i], 
A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child 
of A[i].

Example
Example 1
Input : [3,2,1,4,5]
Output : [1,2,3,4,5]
Explanation : return any one of the legitimate heap arrays

Challenge
O(n) time complexity
"""


# Heapify 的具体实现方法。时间复杂度为 O(n)O(n)，使用的是 siftdown
# 之所以是 O(n) 是因为从第 N/2 个位置开始往下 siftdown，那么就有大约 N/4
# 个数在 siftdown 中最多交换 1 次，N/8 个数最多交换 2 次，N/16 个数最多交换 3 次。
# 所以 O(N/4 * 1 + N/8 * 2 + N/16 * 3 + ... + 1 * LogN) =
# O(N)O(N/4∗1+N/8∗2+N/16∗3+...+1∗LogN)=O(N)
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, index):
        n = len(A)
        while index < n:
            left = index * 2 + 1
            right = index * 2 + 2
            minIndex = index
            if left < n and A[left] < A[minIndex]:
                minIndex = left
            if right < n and A[right] < A[minIndex]:
                minIndex = right
            if minIndex == index:
                break
            A[minIndex], A[index] = A[index], A[minIndex]
            index = minIndex
