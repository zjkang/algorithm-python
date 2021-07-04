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
