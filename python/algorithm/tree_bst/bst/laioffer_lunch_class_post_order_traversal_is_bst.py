'''
Given a sequence of post-order traversal, determine whether the binary tree is binary search tree or not
         5
       3.   8
     1.  4 6  10

post order: 1,4,3,6,10,8,5
'''


def is_bst(nums, start, end):
    if start >= end:
        return True
    cur = start
    while cur < end and nums[cur] < nums[end]:
        cur += 1
    left_end = cur - 1
    while cur < end:
        if nums[cur] < nums[end]:
            return False
        cur += 1
    return is_bst(nums, start, left_end) and is_bst(nums, left_end+1, end-1)


# test
nums = [1, 4, 3, 6, 10, 8, 5]
assert(is_bst(nums, 0, len(nums)-1) is True)
