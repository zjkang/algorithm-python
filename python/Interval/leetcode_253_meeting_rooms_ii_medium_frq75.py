"""
author: Wei Li
date: 10/17/2020

https://leetcode.com/problems/meeting-rooms-ii/

253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
# scan line
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        
        for start, end in intervals:
            points.append((start, 1))
            points.append((end, -1))
        
        on_going = 0
        rooms = 0
        for _, delta in sorted(points):
            on_going += delta
            rooms = max(on_going, rooms)
        
        
        return rooms

# heap
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap, rooms = [], 0
        for start, end in sorted(intervals, key=lambda interval: interval[0]):
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            rooms = max(rooms, len(heap))
        return rooms