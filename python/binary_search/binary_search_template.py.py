# jiuzhang template
# left + 1 < right
# defer the final result to the extra comparison for left & right



# 群主建议模板，和left + 1 < right相比，减少2次left,right最后的额外判断

left, right = 0, sys.maxsize

# template 1
while left < right: # use left < right
  mid = left + (right - left) // 2
  if cond(mid) < k:
    left = mid + 1
  else:
    right = mid

# template 2
while left < right: # use left < right
  mid = right - (right - left) // 2
  if cond(mid) < k:
    left = mid
  else:
    right = mid + 1
    
# 当左边是mid + 1的时候，使用template 1
# 当右边是mid + 1的时候，使用template 2
    
  
