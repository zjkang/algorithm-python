"""
author: Wei Li
date: 10/20/2020

https://leetcode.com/problems/sequence-reconstruction/

444. Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the
sequences in seqs. The org sequence is a permutation of the integers from 1 to
n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common
supersequence of the sequences in seqs (i.e., a shortest sequence so that all
sequences in seqs are subsequences of it). Determine whether there is only
one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:
Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:
Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].

Example 3:
Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:
Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true

Constraints:

1 <= n <= 10^4
org is a permutation of {1,2,...,n}.
1 <= segs[i].length <= 10^5
seqs[i][j] fits in a 32-bit signed integer.
"""


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = self.build_graph(seqs, org)

        if not graph:
            return False

        indegres = self.build_indegres(graph)

        order = self.topo_sort(graph, indegres, org)

        return order == org

    def build_graph(self, seqs, org):
        graph = {}

        for seq in seqs:
            for node in seq:
                if node not in org:
                    return None

                if node not in graph:
                    graph[node] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def build_indegres(self, graph):
        indegres = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                indegres[neighbor] += 1

        return indegres

    def topo_sort(self, graph, indegres, org):
        start_nodes = [node for node in graph if indegres[node] == 0]

        import collections
        queue = collections.deque(start_nodes)
        order = []
        while queue:
            if len(queue) > 1:
                return None
            curr_node = queue.popleft()
            order.append(curr_node)
            for neighbor in graph[curr_node]:
                indegres[neighbor] -= 1
                if indegres[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(org):
            return None

        return order
