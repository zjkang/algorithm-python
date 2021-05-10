'''
author: Zhengjian Kang
date: 05/09/2021

残酷群每日一题: 05/06/2021

https://leetcode.com/problems/minimum-interval-to-include-each-query/

1851. Minimum Interval to Include Each Query

note: PQ + Sorted List + Offline Querying

You are given a 2D integer array intervals, where intervals[i] = [lefti, righti]
describes the ith interval starting at lefti and ending at righti (inclusive).
The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest
interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

Example 1:
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

Example 2:
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
 

Constraints:
1 <= intervals.length <= 10^5
1 <= queries.length <= 10^5
intervals[i].length == 2
1 <= lefti <= righti <= 10^7
1 <= queries[j] <= 10^7
'''


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = [(q, idx) for idx, q in enumerate(queries)]
        queries.sort()
        
        i = 0
        res = [-1] * len(queries)
        from sortedcontainers import SortedList
        sl = SortedList() # sorted list for duration: like c++ mutliset
        pq = [] # PQ: (end, duration) 
        for q in queries:
            while i < len(intervals) and intervals[i][0] <= q[0]:
                duration = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(pq, (intervals[i][1], duration))
                sl.add(duration)
                i += 1
            while pq and pq[0][0] < q[0]:
                sl.remove(pq[0][1])
                heapq.heappop(pq)
            if len(sl):
                res[q[1]] = sl[0]
        return res
            
            
        
