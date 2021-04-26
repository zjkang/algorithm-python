'''
Reference:
https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/hua-dong-chuang-kou-ji-qiao-jin-jie


固定终点写法
如果定义window，收缩window的条件，移动窗口的时机是难点
'''

# 滑动窗口算法框架
def slidingWindow(s: string, t: string):
  need = defaultdict(int)
  window = defaultdict(int)
  
  for c in t:
    need[c] += 1
  
  slow, fast = 0, 0
 
  while fast < len(s):
    # c 是将移入窗口的字符
    c = s[fast]
    
    # 进行窗口内数据的一系列更新
    # ...
    # /*** debug 输出的位置 ***/
    print(f"window: [{left}, {right}]\n")
    
    # 判断左侧窗口是否要收缩
    while (window needs shrink):
      # d 是将移出窗口的字符
      d = s[slow]
      # 左移窗口
      slow += 1
      # 进行窗口内数据的一系列更新
      # ...
    
  # 右移窗口
  fast += 1
