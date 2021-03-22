# decorator
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log
# def now():
#     print('2015-3-25')


# # now = log(now)
# now()

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log('execute')
# def now():
#     print('2015-3-25')


# now = log('execute')(now)
# now()

# ------------------------------------------
# Generator
# 如果列表元素可以按照某种算法推算出来,
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator

# >> > g = (x * x for x in range(10))
# >> > g
# <generator object < genexpr > at 0x1022ef630 >

# >> > next(g)
# 0
# >> > next(g)
# 1

# >> > g = (x * x for x in range(10))
# >> > for n in g:
# ... print(n)


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
