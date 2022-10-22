# _*_coding:utf-8_*_
# created by Amuu on 2022/9/1

import random


def select_sort_simple(li):
    li_new = []  # 非原地排序
    for i in range(len(li)):
        min_val = min(li)  # o(n)
        li_new.append(min_val)
        li.remove(min_val)  # o(n)
    return li_new


def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i  # 无序区第一个数
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
        print(li)

li = [3,2,4,1,5,7,9,6,8]
print(li)
select_sort(li)

