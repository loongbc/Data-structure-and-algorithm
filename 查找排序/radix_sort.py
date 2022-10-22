# _*_coding:utf-8_*_
# created by Amuu on 2021/9/27

# 基数排序（多关键字排序）
def radix_sort(li):
    max_num = max(li)  # 最大值 99->2 ,888->3,10000->5
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            # 987 it = 3 987//100->9%10=9
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 把数重新写回li
        it += 1

# import random
#
# li = [random.randint(0, 100) for i in range(100)]
# radix_sort(li)
# print(li)
