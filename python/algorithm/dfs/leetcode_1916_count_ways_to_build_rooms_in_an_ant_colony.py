"""
author: Zhengjian Kang
date: 07/01/2021

残酷群每日一题: 06/30/2021

https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

1916. Count Ways to Build Rooms in an Ant Colony

note: dfs + math combination/permutation
https://github.com/wisdompeak/LeetCode/tree/master/Math/1916.Count-Ways-to-Build-Rooms-in-an-Ant-Colony

You are an ant tasked with adding n new rooms numbered 0 to n-1 to your colony.
You are given the expansion plan as a 0-indexed integer array of length n, prevRoom,
where prevRoom[i] indicates that you must build room prevRoom[i] before building room i,
and these two rooms must be connected directly. Room 0 is already built, so prevRoom[0] = -1.
The expansion plan is given such that once all the rooms are built, every room will be reachable from room 0.

You can only build one room at a time, and you can travel freely between rooms you have already
built only if they are connected. You can choose to build any room as long as its previous room is already built.

Return the number of different orders you can build all the rooms in. Since the answer may be large, return it modulo 109 + 7.

Example 1:
Input: prevRoom = [-1,0,1]
Output: 1
Explanation: There is only one way to build the additional rooms: 0 → 1 → 2

Example 2:
Input: prevRoom = [-1,0,0,1,2]
Output: 6
Explanation:
The 6 ways are:
0 → 1 → 3 → 2 → 4
0 → 2 → 4 → 1 → 3
0 → 1 → 2 → 3 → 4
0 → 1 → 2 → 4 → 3
0 → 2 → 1 → 3 → 4
0 → 2 → 1 → 4 → 3
 

Constraints:
n == prevRoom.length
2 <= n <= 10^5
prevRoom[0] == -1
0 <= prevRoom[i] < n for all 1 <= i < n
Every room is reachable from room 0 once all the rooms are built.
"""


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(prevRoom):
            g[pre].append(cur)
            
        dp = [0] * 100001
        counts = [0] * 100001
        f = [1] * 100001
        for i in range(1, 100001):
            f[i] = f[i-1] * i % MOD
            
        def inv(x):
            s = 1
            while x > 1:
                s = s * (MOD-MOD//x)%MOD
                x = MOD%x
            return s
        
        def dfs(cur):
            if not g[cur]:
                dp[cur] = 1
                counts[cur] = 1
                return
            
            root_ways, root_num_nodes = 1, 0
            for nei in g[cur]:
                dfs(nei)
                root_ways = root_ways * dp[nei]
                root_num_nodes += counts[nei]
            
            root_ways = (root_ways * f[root_num_nodes]) % MOD
            for nei in g[cur]:
                root_ways = (root_ways * inv(f[counts[nei]])) % MOD
        
            dp[cur] = root_ways
            counts[cur] = root_num_nodes + 1
            
        dfs(0)
        return dp[0] % MOD
