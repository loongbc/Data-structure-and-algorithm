# _*_coding:utf-8_*_
# created by Amuu on 2021/9/27

# 选择排序
import random


def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
        # print(li)

# li = [random.randint(0, 1000) for i in range(1000)]
# print(li)
# select_sort(li)
# print(li)
