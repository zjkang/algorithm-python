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
    
    def __lt__(self, o):
        if self.type != o.type:
            raise Exception('cannot compare for different types')
        if self.type == OrderType.SELL:
            return self.price < o.price
        else:
            return self.price > o.price

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
                heapq.heappush(self.orders_buy, order)
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
                heapq.heappush(self.orders_sell, order)
            
        return rets
        
    
order_exe = OrderExecution()

# # test case 1
# # buy & sell do not match
# # id, type, quantity, price
# orders = [
#     Order(1, OrderType.BUY, 10, 15),
#     Order(2, OrderType.BUY, 8, 20),
#     Order(3, OrderType.SELL, 10, 30) 
# ]
# print('execute', order_exe.execute(orders[0]))
# print('execute', order_exe.execute(orders[1]))
# print('execute', order_exe.execute(orders[2]))
# print('sell after', order_exe.orders_sell)
# print('buy after', order_exe.orders_buy)


# # ------------------------------------------
# # test case 2
# # sell matches buy once, sell is all consumed via one buy
# # id, type, quantity, price
# orders = [
#     Order(1, OrderType.BUY, 10, 15),
#     Order(2, OrderType.BUY, 8, 20),
#     Order(3, OrderType.SELL, 5, 10) 
# ]
# print('execute', order_exe.execute(orders[0]))
# print('execute', order_exe.execute(orders[1]))
# print('execute', order_exe.execute(orders[2]))
# print('sell after', order_exe.orders_sell)
# print('buy after', order_exe.orders_buy)


# ----------------------------------------
# test case 3
# sell matches buy mutliple times, sell is all consumed via multiple buy
# id, type, quantity, price
orders = [
    Order(1, OrderType.BUY, 5, 15),
    Order(2, OrderType.BUY, 8, 20),
    Order(3, OrderType.SELL, 10, 10) 
]
print('execute', order_exe.execute(orders[0]))
print('execute', order_exe.execute(orders[1]))
print('execute', order_exe.execute(orders[2]))
print('sell after', order_exe.orders_sell)
print('buy after', order_exe.orders_buy)

# -----------------------------------------
# # test case 4
# # sell matches buy once, sell is partially consumed via one buy
# # id, type, quantity, price
# orders = [
#     Order(1, OrderType.BUY, 10, 10),
#     Order(2, OrderType.BUY, 8, 20),
#     Order(3, OrderType.SELL, 10, 15) 
# ]
# print('execute', order_exe.execute(orders[0]))
# print('execute', order_exe.execute(orders[1]))
# print('execute', order_exe.execute(orders[2]))
# print('sell after', order_exe.orders_sell)
# print('buy after', order_exe.orders_buy)

#--------------------------------------------- 
        
# class SellOrder(Order):
#     def __init__(self, oid, type, quantity, price):
#         super().__init__(oid, type, quantity, price)
#     def __lt__(self, o):
#         return self.price < o.price  

# class BuyOrder(Order):
#     def __init__(self, oid, type, quantity, price):
#         super().__init__(oid, type, quantity, price)
#     def __lt__(self, o):
#         return self.price > o.price  

# sell -> <= max buy
# buy -> >= min sell

