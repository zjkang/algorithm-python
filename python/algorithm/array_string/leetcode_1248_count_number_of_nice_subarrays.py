'''
1248. Count Number of Nice Subarrays

https://leetcode.com/problems/count-number-of-nice-subarrays/

Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # prefix sum
        pre_sum_map = defaultdict(int)
        pre_sum_map[0] = 1
        total = 0
        res = 0
        for n in nums:
            total += 1 if n % 2 == 1 else 0
            if total - k in pre_sum_map:
                res += pre_sum_map[total-k]
            pre_sum_map[total] += 1
        return res
               

 class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        slow, fast = 0, 0
        num_odd = 0
        res = 0
        count = 0
        while fast < n:
            if nums[fast] % 2 == 1:
                num_odd += 1
                count = 0
            while slow <= fast and num_odd == k:
                if nums[slow] % 2 == 1:
                    num_odd -= 1
                count += 1
                slow += 1
            res += count
            fast += 1
        return res

