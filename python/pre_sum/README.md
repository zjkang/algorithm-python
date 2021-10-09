#### pre-sum 更新

- pre-sum 相关的题目可以考虑一下几个方法

1. prefix sum 的性质 subarray sum index from i to j
   prefix_sum[j] - prefix_sum[i-1]
   加入一个 dummy 初始 prefix_sum[0] = 0
2. max subarray sum - dp 的方法，继承，另起炉灶
3. 双指针 (num > 0)
4. 单调栈和 sliding window

[Leetcode 238 Product of Array Except Self (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_0238_product_of_array_except_self.py)\
[Leetcode 523 Continuous Subarray Sum (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_0523_continuous_subarray_sum_medium.py)\
[Leetcode 974 Subarray Sums Divisible by K (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_0974_subarray_sums_divisible_by_k.py)\
[Leetcode 1442 Count Triplets That Can Form Two Arrays of Equal XOR (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_1442_count_triplets_that_can_form_two_arrays_of_equal_xor.py)\
[Leetcode 1658 Minimum Operations to Reduce X to Zero (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_1658_minimum_operations_to_reduce_x_to_zero.py)\
[Leetcode 1664 Ways to Make a Fair Array (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_1664_ways_to_make_a_fair_array.py)\
[Leetcode 1737 Change Minimum Characters to Satisfy One of Three Conditions (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_1737_change_minimum_characters_to_satisfy_one_of_three_conditions.py)\
[Leetcode 1749 Maximum Absolute Sum of Any Subarray (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_1749_maximum_absolute_sum_of_any_subarray.py)\
[Leetcode 1878 Get Biggest Three Rhombus Sums in a Grid (M)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/leetcode_1878_get_biggest_three_rhombus_sums_in_a_grid.py)

[Lintcode 138 Subarray Sum (E)](https://github.com/zjkang/ds_algorithm/blob/main/python/pre_sum/lintcode_0138_subarray_sum.py)


#### prefix 更新 generalize pre-sum

- prefix 考虑subarray or substring求区间内的性质，可以考虑prefix + hash


