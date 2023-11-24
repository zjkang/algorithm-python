'''
author: Zhengjian Kang

date: 05/05/2021

残酷群每日一题: 05/05/2021

https://leetcode.com/problems/closest-room/

1847. Closest Room

note: heap(sorted set)
offline querying的系列题目

There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms
where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi
and size equal to sizei. Each roomIdi is guaranteed to be unique.

You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej].
The answer to the jth query is the room number id of a room such that:

The room has a size of at least minSizej, and
abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
If there is a tie in the absolute difference, then use the room with the smallest such id.
If there is no such room, the answer is -1.

Return an array answer of length k where answer[j] contains the answer to the jth query.

Example 1:
Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
Output: [3,-1,3]
Explanation: The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.

Example 2:
Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
Output: [2,1,3]
Explanation: The answers to the queries are as follows:
Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.
 

Constraints:

n == rooms.length
1 <= n <= 10^5
k == queries.length
1 <= k <= 10^4
1 <= roomIdi, preferredj <= 10^7
1 <= sizei, minSizej <= 10^7
'''

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        from sortedcontainers import SortedList
        # room[i] = [id, size], query[i] = [preferred, minSize]
        for idx, q in enumerate(queries):
            q.append(idx)
        rooms.sort(key=lambda x: x[1], reverse=True)
        queries.sort(key=lambda x: x[1], reverse=True)
        
        sorted_list = SortedList() 
        i = 0
        res = [0] * len(queries)
        for q in queries:
            min_size = q[1]
            while i < len(rooms) and rooms[i][1] >= min_size:
                sorted_list.add(rooms[i][0])
                i += 1

            if not sorted_list:
                res[q[2]] = -1
                continue
        
            min_id, diff = -1, float('inf')
            index = sorted_list.bisect_left(q[0])
            if index < len(sorted_list) and diff > abs(q[0] - sorted_list[index]):
                diff = abs(q[0] - sorted_list[index])
                min_id = sorted_list[index]
            if index >= 1 and diff >= abs(q[0] - sorted_list[index-1]):
                diff = abs(q[0] - sorted_list[index-1])
                min_id = sorted_list[index-1]
 
            res[q[2]] = min_id
                
        return res 
