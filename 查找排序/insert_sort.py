# _*_coding:utf-8_*_
# created by Amuu on 2021/9/27

# 插入排序

import random


def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        # print(li)


# li = [random.randint(0, 1000) for i in range(1000)]
# print(li)
# insert_sort(li)
# print(li)
