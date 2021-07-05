# 1. the number of connected component between 2 grids
from collections import deque

def bfs(grid, x, y, visited):
    visited[x][y] = True
    queue = deque([(x,y)])
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    M, N = len(grid), len(grid[0])
    flag = 0
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 2:
            flag = 1
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0<= cx < M and 0<= cy < N and not visited[cx][cy] and grid[cx][cy] in [1,2]:
                queue.append((cx,cy))
                visited[cx][cy] = True
    return flag == 1
                
def count_connected_comp(grid1, grid2):
    M, N = len(grid1), len(grid1[0])
    diff_grid = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if grid1[i][j] == grid2[i][j]:
                diff_grid[i][j] = grid1[i][j]
            else:
                diff_grid[i][j] = 2

    visited = [[False] * N for _ in range(M)]
    res = 0
    for i in range(M):
        for j in range(N):
            if diff_grid[i][j] in [1,2] and  not visited[i][j]:
                if not bfs(diff_grid, i, j, visited): # return true if find 2 in the connected component
                    res += 1
    return res
                    
# test cases   
a = [[1,0,0],[0,0,0],[0,1,1]]
b = [[1,0,0],[0,0,0],[0,1,1]]
print(count_connected_comp(a, b))

a = [[1,0,0],[0,0,0],[0,1,1]]
b = [[1,0,0],[0,0,0],[1,1,1]]
print(count_connected_comp(a, b))


# ---------------------------------------------------------------------------------------------
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
    
    
# time = {'A': 1, 'B': 2}
# dependency = {}
# print(build_task(time, dependency))


# given dependency 'A' -> ['B', 'C']
# given tasks execution time {'A': 1, 'B', 2, 'C': 3}
# time = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
# dependency = {'A': ['B', 'C']}
# print(build_task(time, dependency))


# ---------------------------------------------------------------------------------------------
# 3 order execution buy/sell
import heapq
class OrderType:
    BUY = 0
    SELL = 1

class Order:
    def __init__(self, oid, type, quantity, price):
        self.oid = oid
        self.type = type
        self.quantity = quantity
        self.price = price
        
    def __repr__(self):
        str_type = 'buy' if self.type == OrderType.BUY else 'sell'
        return f"order id={self.oid} type={str_type} quantity={self.quantity} price={self.price}"
        
class SellOrder(Order):
    def __init__(self, oid, type, quantity, price):
        super().__init__(oid, type, quantity, price)
    def __lt__(self, o):
        return self.price < o.price  

class BuyOrder(Order):
    def __init__(self, oid, type, quantity, price):
        super().__init__(oid, type, quantity, price)
    def __lt__(self, o):
        return self.price > o.price  
        
# sell -> <= max buy
# buy -> >= min sell

class OrderExecution:
    def __init__(self):
        self.orders_buy = []
        self.orders_sell = []
        
    def execute(self, order):
        rets = []
        if order.type == OrderType.BUY:
            while (
                order.quantity > 0 and \
                self.orders_sell and \
                order.price >= self.orders_sell[0].price
            ):
                if order.quantity < self.orders_sell[0].quantity:
                    rets.append((
                        'sell',
                        self.orders_sell[0].oid,
                        order.quantity,
                        self.orders_sell[0].price
                    ))
                    self.orders_sell[0].quantity -= order.quantity
                    order.quantity = 0
                else:
                    rets.append((
                        'sell', 
                        self.orders_sell[0].oid,
                        self.orders_sell[0].quantity,
                        self.orders_sell[0].price
                    ))
                    order.quantity -= self.orders_sell[0].quantity
                    heapq.heappop(self.orders_sell)
            
            if order.quantity > 0:        
                heapq.heappush(self.orders_buy, BuyOrder(order.oid, order.type, order.quantity, order.price))
        else:
            while (
                order.quantity > 0 and \
                self.orders_buy and \
                order.price <= self.orders_buy[0].price
            ):
                if order.quantity < self.orders_buy[0].quantity:
                    rets.append((
                        'buy',
                        self.orders_buy[0].oid,
                        order.quantity,
                        self.orders_buy[0].price
                    ))
                    self.orders_buy[0].quantity -= order.quantity
                    order.quantity = 0
                else:
                    rets.append((
                        'buy',
                        self.orders_buy[0].oid,
                        self.orders_buy[0].quantity,
                        self.orders_buy[0].price
                    ))
                    order.quantity -= self.orders_buy[0].quantity
                    heapq.heappop(self.orders_buy)
            
            if order.quantity > 0:
                heapq.heappush(self.orders_sell, SellOrder(order.oid, order.type, order.quantity, order.price))
            
        return rets
        
    
# test
# buy & sell do not match
# buy & sell match one order
# buy & sell match >1 order

# quantity, price
orders = [
    Order(1, OrderType.BUY, 10, 15),
    Order(2, OrderType.BUY, 8, 20),
    # Order(3, OrderType.BUY, 20, 10) # no match
    # Order(2, OrderType.BUY, 12, 30), # match>1: sell consumed once, buy all consued
    Order(3, OrderType.BUY, 6, 30) # match: buy all consumed
]
    
order_exe = OrderExecution()

print('--------------------')
print(orders[0])
print('sell before', order_exe.orders_sell)
print('buy before', order_exe.orders_buy)
print('execute', order_exe.execute(orders[0]))
print('sell after', order_exe.orders_sell)
print('buy after', order_exe.orders_buy)

print('--------------------')
print(orders[1])
print('sell before', order_exe.orders_sell)
print('buy before', order_exe.orders_buy)
print('execute', order_exe.execute(orders[1]))
print('sell after', order_exe.orders_sell)
print('buy after', order_exe.orders_buy)
    
print('--------------------')
print(orders[2])
print('sell before', order_exe.orders_sell)
print('buy before', order_exe.orders_buy)
print('execute', order_exe.execute(orders[2]))
print('sell after', order_exe.orders_sell)
print('buy after', order_exe.orders_buy)
