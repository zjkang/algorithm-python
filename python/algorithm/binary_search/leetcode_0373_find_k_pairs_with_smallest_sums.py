"""
author: Zhengjian Kang

date: 10/25/2021
残酷群每日一题: 10/24/2021

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

373. Find K Pairs with Smallest Sums

note: binary search by value or use heap

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:
1 <= nums1.length, nums2.length <= 10^5
-109 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 1000
"""

# heap
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        pq = [(nums1[0] + nums2[0], 0, 0)]
        # why 2D array TLE but set not cause?
        visited = set([(0,0)])
        
        res = []
        for _ in range(k):
            if not pq: break
            v, i1, i2 = heapq.heappop(pq) 

            res.append([nums1[i1], nums2[i2]])
            if i1+1 < m and (i1+1,i2) not in visited:
                heapq.heappush(pq, (nums1[i1+1]+nums2[i2], i1+1, i2))
                visited.add((i1+1,i2))
                
            if i2+1 < n and (i1,i2+1) not in visited:
                heapq.heappush(pq, (nums1[i1]+nums2[i2+1], i1, i2+1))
                visited.add((i1,i2+1))
            
        return res

# binary search
# c++
# class Solution {    
# public:
#     vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) 
#     {
#         long left = INT_MIN, right = INT_MAX;
#         while (left < right)
#         {
#             long mid = left+(right-left)/2;
#             long count = countSmallerOrEqual(mid, nums1, nums2);
#             if (count < k)
#                 left = mid+1;
#             else
#                 right = mid;
#         }
#         int m = left;

#         // TODO-TLE: nums1 = [1] * 100000, nums2 = [1] * 100000, k = 2
#         vector<vector<int>>rets;
#         for (int i=0; i<nums1.size(); i++)
#         {
#             for (int j = 0; j<nums2.size() && nums1[i]+nums2[j]<m; j ++)
#             {
#                 rets.push_back({nums1[i], nums2[j]});
#             }                
#         }
        
#         // 316ms/11.89% -> 148ms/43.01%
#         for (int i=0; i<nums1.size(); i++)
#         {
#             for (int j = 0; j<nums2.size() && nums1[i]+nums2[j]<=m && rets.size() < k; j ++)
#             {
#                 if (nums1[i]+nums2[j]==m) {
#                     rets.push_back({nums1[i], nums2[j]});
#                 }
#             }                
#         }        
        
#         return rets;
#     }

#     long countSmallerOrEqual(int m, vector<int>& nums1, vector<int>& nums2)
#     {
#         int j = nums2.size()-1;
#         long ret = 0;
#         for (int i=0; i<nums1.size(); i++)
#         {
#             while (j>=0 && nums1[i]+nums2[j]>m)
#                 j--;
#             ret += j+1;
#         }
#         return ret;
#     }
# };
 
