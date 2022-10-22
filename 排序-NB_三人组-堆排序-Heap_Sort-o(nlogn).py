# _*_coding:utf-8_*_
# created by Amuu on 2022/9/1

def sift(li, low, high):
    """

    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子有并且比左孩子大
            j += 1  # 把j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1  # 新的左孩子
        else:  # tmp 更大 ，把 tmp 放到 i 的位置
            li[i] = tmp  # 把tmp放到某一级领导位置
            break
    else:
        li[i] = tmp  # 把 tmp 放到叶子节点上


def heap_sort(li):
    n = len(li)
    # 怎么建立堆： 农村包围城市 首先找到最后一个非叶子节点
    for i in range((n - 2) // 2, -1, -1):  # i 表示建堆时候调整的部分的根的下标
        sift(li, i, n - 1)
    # 建堆完成

    for i in range(n - 1, -1, -1):  # i 指向当先堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1 是新的 high


li = [i for i in range(100)]
import random

random.shuffle(li)

print(li)
# heap_sort(li)
# print(li)

# 堆排序内置模块

import heapq  # q-> queue 优先队列

heapq.heapify(li)  # 建小根堆
for i in range(len(li)):
    print(heapq.heappop(li), end=',')

