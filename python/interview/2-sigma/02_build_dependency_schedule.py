# 2. build dependency schedule
# round 3： 口音很奇怪的一个人（不是三哥，问了问其他人，觉得可能是个意大利人...），没开视频，顿时觉得要完...
# 结果也是载在了这道题上。给一系列tasks，每个task有parent和运行时间。task的执行必须是在其parents都结束之后，并且tasks可以并行执行。打印出执行时间和顺序
# 我最后在他的提示下做出来了。题和答案我都会整理在gitbook中，等过整理好了贡献出来。
# 写过code，找不到在哪里了...
# 大概是
# process order, task name array, number of unit time
# 比如
# 1 A,B,E 2
# 2 B,E 1
# 3 E,D 3

# xiaojdaha 发表于 2020-11-5 03:24
# 谢谢楼主，请问第三题应该用什么方法解呢？已加米

# 得用到图。（很意外leetcode为何没有，这题见过至少两遍了...）
# 建立好一个有向图之后，找到所有没有parent的点 [P]， 循环做以下操作
#     1. 在【P】中找出最少的时间 t
#     2. 输出这些点最小时间 t P_1, P_2, ...
#     3. 把【P】中所有节点的时间减 t
#     4. 从图中去掉所有时间为0的点， 同时从【P】中去掉这些点，并将其没有父节点的子节点加入 【P】
# 其实我觉得代码没有练习直接写出来很不容易...算是一道压轴题吧.

# given dependency 'A' -> ['B', 'C']
# given tasks execution time {'A': 1, 'B', 2, 'C': 3}

# given dependency None
# given tasks execution time {'A': 1, 'B': 2}

from collections import defaultdict
import heapq

def build_task(time, dependency):
    # build graph for topo
    indegree = {tk: 0 for tk in time}
    graph = defaultdict(list)
    for k, v in dependency.items():
        graph[k] = v
        for node in v:
            indegree[node] += 1
    # priority-queue for sort
    pq = []
    for node in indegree:
        if indegree[node] == 0:
            heapq.heappush(pq, (time[node], node))
    rets = []
    while pq:
        t, n = pq[0]
        level = [t]
        temp = []
        while pq:
            ct, cn = heapq.heappop(pq)
            level.append(cn)
            if ct - t == 0:
                # can start to execute dependent task
                for nei in graph[cn]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        temp.append((time[nei], nei))
            else:
                temp.append((ct - t, cn))
        pq = temp
        heapq.heapify(pq)
        rets.append(level)
    
    return rets
    
    
time = {'A': 1, 'B': 2}
dependency = {}
print(build_task(time, dependency))

# given dependency 'A' -> ['B', 'C']
# given tasks execution time {'A': 1, 'B', 2, 'C': 3}
time = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
dependency = {'A': ['B', 'C']}
print(build_task(time, dependency))
