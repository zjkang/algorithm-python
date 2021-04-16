# 0分钟， 平台是Hackerrank CodePair + 电话。注: CodePair里面是没有正规的debugger的。
# 上来interviewer说时间紧。我们先做题。面试题目如下，喜欢求赏大米。

# 实现一个随机数生成， 支持下面的两个函数
# set_range: 设定生成随机数的区间
# get_random: 生成随机数。要求生成的数在区间之内。并且，生成的数在区间内所有的数字都被生成返回之前不可重复。
# 实现这个类，并写测试。

# 追加问题：
# 时间的复杂度是多少？
# 如果用户可以在一系列get_random中间，叫set_range, 如何保持get_random生成的数的属性？

# 解法：
# 实例变量记录下已生成的数。
# 每次set_range里面生成一个数组里面有区间里的所有数，除了那些已经生成过的数
# get_random里随机选一个数组里的数输出，并从数组移除返回的数。
# （数的移除是可以在恒定时间里实现的）

import random
class RandomGenerator:
    def __init__(self):
        self.nums = []
        self.index = -1
    
    def set_range(self, lower, upper):
        if self.index >= 0:
            raise Exception("Cannot set range")
        self.nums = [i for i in range(lower, upper+1)]
        self.index = upper - lower
        
    def get_random(self):
        if self.index < 0:
            raise Exception("find all random numbers")
        idx = random.randint(0, self.index)
        rand_num = self.nums[idx]
        self.nums[idx], self.nums[self.index] = self.nums[self.index], self.nums[idx]
        self.index -= 1
        return rand_num
    
# test
r = RandomGenerator()
r.set_range(1,5)
print(r.get_random())
print(r.get_random())
print(r.get_random())
print(r.get_random())
print(r.get_random())
print(r.get_random())

# init w/o init the whole array
class RandomGenerator:
    def __init__(self, lower, upper):
        self.seen = {}
        self.lower = lower
        self.upper = upper
        
    def get_random(self):
        if self.upper < 0:
            raise Exception('Already generate all numbers')
        num = random.randint(self.lower, self.upper)
        ret = num
        if num in self.seen:
            ret = self.seen[num]
        self.seen[num] = self.seen[self.upper] if self.upper in self.seen else self.upper
        self.upper -= 1
        return ret
    


# -----------------------------------------------------
# follow up
import random
class RandomGenerator:
    def __init__(self):
        self.nums = []
        self.index = -1
    
    def set_range(self, lower, upper):
        visited = []
        if self.index >= 0:
            visited = [i for i in self.nums[self.index+1:] if i >= lower and i <= upper]
        self.nums = [i for i in range(lower, upper+1)]
        self.index = upper - lower
        for v in visited:
            idx = v - lower
            self.swap(idx, self.index)
            self.index -= 1
                    
    def swap(self, idx1, idx2):
        self.nums[idx1], self.nums[idx2] = self.nums[idx2], self.nums[idx1]
        
    def get_random(self):
        if self.index < 0:
            raise Exception("find all random numbers")
        idx = random.randint(0, self.index)
        rand_num = self.nums[idx]
        self.swap(idx, self.index)
        self.index -= 1
        return rand_num
    
# test
r = RandomGenerator()
r.set_range(3,5)
print(r.get_random())
print(r.get_random())
r.set_range(2,6)
print(r.get_random())
print(r.get_random())
print(r.get_random())
print(r.get_random())
