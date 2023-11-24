'''
1004. Max Consecutive Ones III

https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # sliding window
        res = 0
        slow, fast = 0, 0
        while fast < len(A):
            if A[fast] == 0:
                K -= 1
            while slow <= fast and K < 0:
                if A[slow] == 0:
                    K += 1
                slow += 1
            res = max(res, fast - slow + 1)
            fast += 1
        return res
