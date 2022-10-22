# _*_coding:utf-8_*_
# created by Amuu on 2021/9/26

# 堆排序 o（logn）
def sift(li, low, high):  # 列表 堆的根节点位置 堆的最后一个元素的位置
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j 开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # j 指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1  # 新的左孩子
        else:  # tmp 更大 ，把 tmp 放到 i 的位置
            li[i] = tmp
            break
    else:
        li[i] = tmp  # 把 tmp 放到叶子节点上


def heap_sort(li):
    n = len(li)
    # 怎么建立堆： 农村包围城市 首先找到最后一个非叶子节点
    for i in range((n - 2) // 2, -1, -1):  # i 表示建堆时候调整的部分的根的下标
        sift(li, i, n - 1)
        # 建堆完成
    # print(li)
    for i in range(n - 1, -1, -1):  # i 指向当先堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-4 是新的 high


# li = [i for i in range(100)]
# import random
# random.shuffle(li)
# print(li)
#
# heap_sort(li)
# print(li)

# import heapq # q-> queue 优先队列
# import random
#
# li = list(range(100))
# random.shuffle(li)
# print(li)
#
# heapq.heapify(li) # 建小根堆
#
# n = len(li)
# for i in range(n):
#     print(heapq.heappop(li),end=',')
'''
堆排序------topk 问题  ：现在有 n 个数，设计算法得到前 k 大的数。（k<n)
----------排序后切片 o（nlogn）
----------排序LowB三人组 o（kn）
----------堆排序思路 o（nlogk）
'''
