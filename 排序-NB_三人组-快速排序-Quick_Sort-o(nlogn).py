# _*_coding:utf-8_*_
# created by Amuu on 2022/9/1

import random
import copy
from cal_time import *
import sys

sys.setrecursionlimit(1000000)  # 递归最大深度


def partition(li, left, right):  # o(n)
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1  # 往右走一步
        li[left] = li[right]  # 把右边的值写到左边空位上
        print(li, 'right', right)
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边空位上
        print(li, 'left', left)
    li[left] = tmp  # 把tmp归位
    return left


def _quick_sort(li, left, right):  # 递归  o(logn)
    if left < right:  # 至少两个元素
        mid = partition(li, left, right)  # P归位
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


li = list(range(2000,0,-1))
# random.shuffle(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li = [5,7,4,6,3,1,2,9,8]
# li = [2,1,4,3,5]
# print(li1)
quick_sort(li)
print(li)
# bubble_sort(li2)
# print(li)

# #  快排最坏情况 倒序 o(n2)
#
# li = [9,8,7,6,5,4,3,2,1]
# print(li)
# quick_sort(li)
# print(li)
