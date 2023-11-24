

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
