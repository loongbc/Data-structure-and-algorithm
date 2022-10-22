# _*_coding:utf-8_*_
# created by Amuu on 2022/8/31

from cal_time import *


@cal_time
def Linear_Search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None


@cal_time
def Binary_Search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:  # 候选区有人
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # li[mid] < val 待查找的值在mid右侧
            left = mid + 1
    else:
        return None


li = list(range(10000))
Linear_Search(li, 3890)
Binary_Search(li, 3890)
