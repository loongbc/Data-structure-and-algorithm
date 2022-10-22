# _*_coding:utf-8_*_
# created by Amuu on 2021/9/27

import sys, random, copy

from cal_time import *

sys.setrecursionlimit(100000)  # 递归最大深度


@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None


@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


@cal_time
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
        # print(li)


@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        # print(li)\


@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1  # 往右走一步
        li[left] = li[right]  # 把右边的值写到左边空位上
        # print(li, 'right', right)
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边空位上
        # print(li, 'left', left)
    li[left] = tmp  # 把tmp归位
    return left


def _quick_sort(li, left, right):
    if left < right:  # 至少两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@cal_time
def quick_sort(li):  # 迭代部分用此方法
    _quick_sort(li, 0, len(li) - 1)


li = list(range(10000))
random.shuffle(li)
lis = [copy.deepcopy(li) for i in range(6)]
linear_search(lis[0], 100)
binary_search(lis[1], 100)
select_sort(lis[2])
insert_sort(lis[3])
quick_sort(lis[4])
insert_sort(lis[5])
